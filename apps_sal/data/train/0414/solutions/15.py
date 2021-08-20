from collections import deque, defaultdict


class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        dq = deque()
        count = defaultdict(lambda: 0)
        for ele in arr:
            dq.append(ele)
        while True:
            x = dq.popleft()
            y = dq.popleft()
            if x > y:
                maxv = x
                minv = y
            else:
                maxv = y
                minv = x
            count[maxv] += 1
            if count[maxv] == k:
                return maxv
            dq.append(minv)
            dq.appendleft(maxv)
