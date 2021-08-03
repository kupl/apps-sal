class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        '''
        for arr[k:k+m], it forms m-group if max(time[x] for x in range(k,k+m) < min(time[k-1],time[k+m]),  )
        cand(k)=
        '''
        turnedOnTime = {}
        for i, x in enumerate(arr):
            turnedOnTime[x] = i + 1
        n = len(arr)
        q = deque()
        ans = -1
        for i in range(1, n + 1):
            while q and q[0][0] < i - m + 1:
                q.popleft()
            while q and q[-1][1] <= turnedOnTime.get(i, n + 1):
                q.pop()
            q.append((i, turnedOnTime.get(i, n + 1)))
            if i >= m:
                vanishTime = min(turnedOnTime.get(i + 1, n + 1), turnedOnTime.get(i - m, n + 1))
                cur = -1 if q[0][1] >= vanishTime else (vanishTime - 1)
                ans = max(ans, cur)
        return ans
