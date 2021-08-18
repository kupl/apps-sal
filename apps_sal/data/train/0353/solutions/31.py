class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        N = 10 ** 9 + 7
        D = [1] * (len(nums) + 1)

        def bisect(x, low, high):
            if high - low <= 1:
                if nums[high] <= x:
                    return high
                else:
                    return low

            mid = (low + high) // 2
            if nums[mid] <= x:
                return bisect(x, mid, high)
            else:
                return bisect(x, low, mid)

        for idx in range(1, len(D)):
            D[idx] = D[idx - 1] * 2

        n = len(nums) - 1
        for idx, i in enumerate(nums):
            if i > target - i:
                break
            else:
                best = bisect(target - i, idx, n)
                n = best
                cnt += D[best - idx]

        return cnt % N
