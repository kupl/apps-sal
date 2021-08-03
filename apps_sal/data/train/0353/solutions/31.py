class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sub sequence 就随便排序了，
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

        # generate combination number
        for idx in range(1, len(D)):
            D[idx] = D[idx - 1] * 2

        # print (D)

        n = len(nums) - 1
        for idx, i in enumerate(nums):
            if i > target - i:
                break
            else:
                # print(target - i, idx, n)
                best = bisect(target - i, idx, n)
                # print ('best', best, 'idx', idx)
                n = best
                cnt += D[best - idx]

        # print (D)
        return cnt % N
