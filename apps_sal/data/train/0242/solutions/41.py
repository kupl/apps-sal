class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = {}
        num = {}
        m = 0
        for i in range(len(nums)):
            if nums[i] in num:
                num[nums[i]] += 1
                if num[nums[i]] in freq:
                    freq[num[nums[i]]] += 1
                    if num[nums[i]] - 1 in freq:
                        freq[num[nums[i]] - 1] -= 1
                    if num[nums[i]] - 1 in freq and freq[num[nums[i]] - 1] == 0:
                        freq.pop(num[nums[i]] - 1)
                else:
                    freq[num[nums[i]]] = 1
                    if num[nums[i]] - 1 in freq:
                        freq[num[nums[i]] - 1] -= 1
                    if num[nums[i]] - 1 in freq and freq[num[nums[i]] - 1] == 0:
                        freq.pop(num[nums[i]] - 1)
            else:
                num[nums[i]] = 1
                if 1 in freq:
                    freq[1] += 1
                    if 0 in freq and freq[0] == 0:
                        freq.pop(0)
                else:
                    freq[1] = 1
                    if 0 in freq and freq[0] == 0:
                        freq.pop(0)
            if len(freq) == 1 and 1 in freq:
                m = i + 1
            elif len(freq) == 2:
                a = list(freq.keys())
                b = max(a)
                c = min(a)
                if b - c == 1 and freq[b] == 1:
                    m = i + 1
                if 1 in freq and freq[1] == 1:
                    m = i + 1
        if len(freq) == 1 and len(set(nums)) == 1:
            return len(nums)
        return m
