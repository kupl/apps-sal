class Solution:
    def maxEqualFreq(self, nums) -> int:
        res = maxFrq = 0
        count = defaultdict(int)
        freq = defaultdict(int)
        for i, num in enumerate(nums):
            cnt = count[num]
            freq[cnt] -= 1
            
            cnt += 1
            count[num] = cnt

            freq[cnt] += 1
            maxFrq = max(maxFrq, cnt)
            if (maxFrq == 1) or (maxFrq*freq[maxFrq]) == i or ((maxFrq-1)*(freq[maxFrq-1] + 1)) == i:
                res = i + 1
        return res


