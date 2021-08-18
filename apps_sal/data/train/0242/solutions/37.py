class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        res = 0
        numToCount = {}
        countToNum = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in numToCount:
                numToCount[num] = 0
            count = numToCount[num]
            if count != 0:
                countToNum[count].remove(num)
                if len(countToNum[count]) == 0:
                    del countToNum[count]
            count += 1
            if count not in countToNum:
                countToNum[count] = set()
            countToNum[count].add(num)
            numToCount[num] = count
            if len(countToNum) == 1:
                if count == 1 or len(countToNum[count]) == 1:
                    res = i + 1
            elif len(countToNum) == 2:
                keys = sorted(list(countToNum.keys()))
                if (keys[0] == 1 and len(countToNum[keys[0]])) == 1 or (keys[0] + 1 == keys[1] and len(countToNum[keys[1]]) == 1):
                    res = i + 1
        return res
