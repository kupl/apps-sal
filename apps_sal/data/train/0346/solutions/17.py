class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s = 0
        e = 0
        l = len(nums)
        total = 0
        num_odd = 0
        ae = 0
        while s < l:

            while e < l and num_odd != k:
                if nums[e] % 2 != 0:
                    num_odd += 1

                e += 1

            if num_odd == k:
                if ae < e:
                    ae = e
                    while ae < l and nums[ae] % 2 == 0:
                        ae += 1
                total += (ae - (e - 1))

            if nums[s] % 2 != 0:
                num_odd -= 1
            s += 1

        return total
