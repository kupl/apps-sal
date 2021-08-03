class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        record = [0] * n
        flip = 0
        ans = 0
        for i in range(n):
            if i >= K:
                flip -= record[i - K]
            if A[i] == (flip % 2):
                if i > n - K:
                    return -1
                ans += 1
                flip += 1
                record[i] = 1
        return ans
