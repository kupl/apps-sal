class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counterCounter = defaultdict(int)
        numCounter = defaultdict(int)
        ans = 0
        maxRepeat = 0
        for i, num in enumerate(nums):
            numCounter[num] += 1
            counterCounter[numCounter[num]] += 1
            maxRepeat = max(numCounter[num], maxRepeat)
            if numCounter[num] > 1:
                counterCounter[numCounter[num] - 1] -= 1
            if (counterCounter[maxRepeat] == 1 and (maxRepeat - 1) * (counterCounter[maxRepeat - 1] + 1) == i) or (counterCounter[1] == 1 and (maxRepeat) * (counterCounter[maxRepeat]) == i):
                ans = i + 1
            if maxRepeat == 1 or maxRepeat == i + 1:
                ans = i + 1

            # print(counterCounter, maxRepeat)
        return ans
