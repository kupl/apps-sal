class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefix[i + 1] = prefix[i] + A[i]

        monoq = deque()
        ans = len(prefix)
        for i, p in enumerate(prefix):
            while monoq and prefix[monoq[-1]] >= p:
                monoq.pop()
            while monoq and p - prefix[monoq[0]] >= K:
                ans = min(ans, i - monoq.popleft())
            monoq.append(i)

        return ans if ans < len(prefix) else -1
