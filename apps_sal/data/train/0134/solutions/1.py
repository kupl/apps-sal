class Solution:

    def numDupDigitsAtMostN(self, N: int) -> int:

        def numPerm(n, r):
            return math.factorial(n) // math.factorial(n - r)
        nums = [int(d) for d in str(N + 1)]
        K = len(nums)
        cnt = 0
        for i in range(1, K):
            cnt += 9 * numPerm(9, i - 1)
        seen = set()
        for i in range(K):
            for x in range(1 if i == 0 else 0, nums[i]):
                if x in seen:
                    continue
                cnt += numPerm(10 - (i + 1), K - (i + 1))
            if nums[i] in seen:
                break
            seen.add(nums[i])
        return N - cnt
