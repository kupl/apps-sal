class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter, pattern = {}, {}
        rtn = 0
        if len(nums) <= 3:
            return len(nums)
        for i in range(len(nums)):
            n = nums[i]
            if n in counter:
                t = counter[n]
                counter[n] += 1
            else:
                t = 0
                counter[n] = 1
                
            if t > 0:
                pattern[t] -= 1
                if pattern[t] == 0:
                    del pattern[t]
                
            if t+1 in pattern:
                pattern[t+1] += 1
            else:
                pattern[t+1] = 1
            if len(pattern) == 1:
                for k, v in list(pattern.items()):
                    if k == 1 or v == 1:
                        rtn = max(rtn, i)
            elif len(pattern) == 2:
                if 1 in pattern and pattern[1] == 1:
                    rtn = max(i, rtn)
                [m1, m2] = [(k,v) for k,v in list(pattern.items())]
                if (m1[0] - m2[0] == 1 and m1[1] == 1) or (m2[0] - m1[0] == 1 and m2[1] == 1):
                    rtn = max(rtn, i)
        return rtn + 1

