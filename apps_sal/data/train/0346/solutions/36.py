class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [0] * len(nums)
        n = len(nums)
        d = {}
        if nums[0] % 2 == 1:
            odds[0] = 1
        else:
            odds[0] = 0

        odds = [0] + odds
        d[0] = d.setdefault(0, []) + [0]

        count = 0
        for i in range(1, n + 1):
            if nums[i - 1] % 2 == 1:
                odds[i] = odds[i - 1] + 1
            else:
                odds[i] = odds[i - 1]

            if odds[i] - k in d:
                count += len(d[odds[i] - k])
            d[odds[i]] = d.setdefault(odds[i], []) + [i]

        return (count)
