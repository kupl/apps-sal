class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        countMap, freqMap, maxFreq, maxIndex = defaultdict(int), defaultdict(int), 0, 0

        for index, x in enumerate(nums):
            freqMap[countMap[x]] -= 1
            countMap[x] += 1
            freqMap[countMap[x]] += 1

            maxFreq = max(maxFreq, countMap[x])

            if maxFreq * freqMap[maxFreq] == index or (maxFreq - 1) * (freqMap[maxFreq - 1] + 1) == index or maxFreq == 1:
                maxIndex = index + 1

        return maxIndex
