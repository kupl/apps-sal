from collections import deque


class Solution:
    def findLatestStep(self, lis: List[int], m: int) -> int:
        n = len(lis)
        if m > n:
            return 0
        if m == n:
            return n
        if n == 1:
            return 1
        lis = [[lis[i], i] for i in range(n)]
        lis.sort()
        # print(lis)
        q = deque()
        ans = 0
        for i in range(n):
            while q and lis[i][1] >= q[-1][0]:
                q.pop()
            q.append([lis[i][1], i])
            while q and q[0][1] <= i - m:
                q.popleft()
            if i >= m - 1:
                aa = q[0][0]
          #      print(aa,i,m)
                if i == m - 1:
                    if i + 1 < n and aa < lis[i + 1][1]:
                        ans = max(ans, lis[i + 1][1])
                if i == n - 1:
                    # print(lis[i-m][1],i,m)
                    if aa < lis[i - m][1]:
                        ans = max(ans, lis[i - m][1])
                else:
                    if i + 1 < n and aa < lis[i + 1][1] and aa < lis[i - m][1]:
                        ans = max(ans, min(lis[i + 1][1], lis[i - m][1]))
                # print(ans)
        return -1 if ans == 0 else ans
