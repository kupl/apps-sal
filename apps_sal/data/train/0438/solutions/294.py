class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        visited = [0 for _ in range(n)]
        d = [0 for _ in range(n)]
        
        cnt = 0
        ans = -1
        for step, i in enumerate(arr):
            i = i-1
            lhs, rhs = 0, 0
            start, end = i, i
            visited[i] = 1
            if i+1 < n and visited[i+1]:
                rhs = d[i+1]
                end = i + rhs
                if rhs == m:
                    cnt -= 1
            if i- 1 >= 0 and visited[i-1]:
                lhs = d[i-1]
                start = i - lhs
                if lhs == m:
                    cnt -= 1
                    
            length = lhs + rhs + 1
            d[start] = length
            d[end] = length
            # print(start, end, length)
            if length == m:
                cnt += 1
            if cnt > 0:
                ans = step+1
            # print(cnt)
        
        return ans

