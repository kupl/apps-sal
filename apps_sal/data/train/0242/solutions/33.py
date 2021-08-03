class Solution:
    def maxEqualFreq(self, nums) -> int:
        res = maxFrq = 0
        count = defaultdict(int)
        freq = defaultdict(int)
        for i in range(len(nums)):
            cnt = count[nums[i]]
            freq[cnt] -= 1
            count[nums[i]] += 1

            cnt = count[nums[i]]
            freq[cnt] += 1
            maxFrq = max(maxFrq, count[nums[i]])
            if (maxFrq == 1) or (maxFrq * freq[maxFrq]) == i or ((maxFrq - 1) * (freq[maxFrq - 1] + 1)) == i:
                res = i + 1
        return res
