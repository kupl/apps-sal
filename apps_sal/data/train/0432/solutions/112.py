class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        numDict = {}
        for num in nums:
            if str(num) in numDict:
                numDict[str(num)] += 1
            else:
                numDict[str(num)] = 1
        for key in sorted(list(numDict.keys()), key=lambda x: int(x)):
            val = numDict[key]
            if val == 0:
                continue
            for i in range(1, k):
                if str(int(key) + i) not in numDict:
                    return False
                temp = numDict[str(int(key) + i)] - val
                if temp < 0:
                    return False
                numDict[str(int(key) + i)] = temp
        return True
