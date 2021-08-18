class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        s = collections.deque()
        curr = 0
        ans = math.inf
        for i in range(len(A)):
            curr += A[i]
            if curr >= k:
                ans = min(ans, i + 1)
            while s and curr - s[0][0] >= k:
                ans = min(ans, i - s.popleft()[1])
            while s and s[-1][0] > curr:
                s.pop()
            s.append((curr, i))

        return ans if ans != float('inf') else -1
