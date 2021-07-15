class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        flipped = [0 for _ in range(N)]
        curr = 0
        ans = 0
        for i in range(N):
            if i >= K:
                curr ^= flipped[i - K]
            if curr == A[i]:
                if i + K > N:
                    return -1
                flipped[i] = 1
                curr ^= 1
                ans += 1
        return ans
