class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        s = sum(nums)
        rem = s % p

        i, j, curr_rem = 0, 0, 0
        mi = float('inf')
        d = {0: -1}
        while i < len(nums):
            curr_rem = (curr_rem + nums[i]) % p
            d[curr_rem] = i
           # print(curr_rem,rem)
            if (curr_rem - rem) % p in d:
               # print()
                mi = min(mi, i - d[(curr_rem - rem) % p])
               # print(\"yes\",i,(curr_rem-rem)%p,d)
            i += 1

        return mi if mi != len(nums) else -1
