class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        ret = 0

        for i in range(ln):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0

        # print(nums)

        mp = {0: 1}
        cnt = 0

        for n in nums:
            cnt += n

            if cnt not in mp:
                mp[cnt] = 0
            mp[cnt] += 1

            if cnt - k in mp:
                ret += mp[cnt - k]

        return ret
        pass
