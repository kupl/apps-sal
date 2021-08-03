class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        num_freq = {}
        freq_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        for f in num_freq.values():
            freq_freq[f] = freq_freq.get(f, 0) + 1

        n = len(nums)
        if len(freq_freq) == 2:
            key1, key2 = list(freq_freq.keys())
            if freq_freq[key1] == 1 and (key1 == 1 or key1 == key2 + 1):
                return n
            if freq_freq[key2] == 1 and (key2 == 1 or key2 == key1 + 1):
                return n
        if len(freq_freq) == 1:
            key = list(freq_freq.keys())[0]
            if key == 1 or freq_freq[key] == 1:
                return n

        for i in range(n):
            num = nums[n - i - 1]
            prev_freq = num_freq[num]
            num_freq[num] -= 1
            freq_freq[prev_freq] -= 1
            if freq_freq[prev_freq] == 0:
                del freq_freq[prev_freq]
            if num_freq[num] != 0:
                freq_freq[num_freq[num]] = freq_freq.get(num_freq[num], 0) + 1
            if len(freq_freq) == 2:
                key1, key2 = list(freq_freq.keys())
                if freq_freq[key1] == 1 and (key1 == 1 or key1 == key2 + 1):
                    return n - i - 1
                if freq_freq[key2] == 1 and (key2 == 1 or key2 == key1 + 1):
                    return n - i - 1
            if len(freq_freq) == 1:
                key = list(freq_freq.keys())[0]
                if key == 1 or freq_freq[key] == 1:
                    return n - i - 1
        return 0
