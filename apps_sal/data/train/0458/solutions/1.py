class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        curr_acc_sum = sum(nums)
        rem = curr_acc_sum % p
        if rem == 0:
            return 0
        h_rem, min_len = {0: -1}, len(nums)
        cur_rem = 0
        for i in range(len(nums)):
            cur_rem = (cur_rem + nums[i]) % p
            h_rem[cur_rem] = i
            # print([rem, cur_rem, (cur_rem - rem) % p])
            if (cur_rem - rem) % p in h_rem:
                # print([min_len, i - h_rem[(cur_rem - rem) % p]])
                min_len = min(min_len, i - h_rem[(cur_rem - rem) % p])
        if min_len == len(nums):
            return -1
        return min_len
