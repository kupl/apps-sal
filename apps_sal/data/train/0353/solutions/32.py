class Solution:
    def __init__(self):
        mod = 1e9 + 7
        self.two_power = [0] * 100010
        self.two_power[0] = 1
        for i in range(1, len(self.two_power)):
            num = self.two_power[i - 1] * 2
            if num > mod:
                num %= mod
            self.two_power[i] = num

    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 1e9 + 7
        nums = sorted(nums)
        sind = 0
        eind = len(nums) - 1
        ans = 0

        # print(self.two_power[:20])

        while sind <= eind:
            if nums[sind] + nums[eind] > target:
                eind -= 1
            else:
                ans += self.two_power[eind - sind]
                if ans > mod:
                    ans %= mod
                sind += 1
        return int(ans)
