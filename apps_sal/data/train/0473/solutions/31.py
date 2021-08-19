class Solution:

    def countTriplets(self, arr: List[int]) -> int:

        @lru_cache(None)
        def xor_reduce(i, j):
            if j - i == 1:
                return arr[i] ^ arr[j]
            else:
                return xor_reduce(i + 1, j) ^ arr[i]
        ans = 0
        N = len(arr)
        for i in range(N):
            for j in range(i + 1, N):
                x = xor_reduce(i, j)
                if x == 0:
                    ans += j - i
        return ans
