class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        mem = {}

        def getFactors(num: int) -> set:
            if num in mem:
                return mem[num]
            for divBy in range(2, floor(sqrt(num)) + 1):
                if num % divBy == 0:
                    mem[num] = getFactors(num // divBy) | set([divBy])
                    return mem[num]
            mem[num] = set([num])
            return mem[num]

        groups = {}
        factorToNum = {}
        numToGroupKey = {}
        groupKeyToNums = defaultdict(lambda: [])

        def findGroupsForFactors(factors: List[int]) -> List[int]:
            keys = set()
            for factor in factors:
                if factor in factorToNum:
                    keys.add(numToGroupKey[factorToNum[factor]])
            return keys

        maxSize = 0
        for num in A:
            factors = getFactors(num)
            groupKeys = findGroupsForFactors(factors)
            for factor in factors:
                factorToNum[factor] = num
            size = 1 + sum([groups[key] for key in groupKeys])
            if len(groupKeys) >= 2:
                numToGroupKey[num] = num
                groupKeyToNums[num] = [num]
                for key in groupKeys:
                    for lastNum in groupKeyToNums[key]:
                        numToGroupKey[lastNum] = num
                        groupKeyToNums[num].append(lastNum)
                    groupKeyToNums[num].append(key)
                    del groupKeyToNums[key]
                    del groups[key]
                groups[num] = size
            elif len(groupKeys) == 1:
                otherGroup = list(groupKeys)[0]
                numToGroupKey[num] = otherGroup
                groupKeyToNums[otherGroup].append(num)
                groups[otherGroup] = size
            else:
                numToGroupKey[num] = num
                groupKeyToNums[num] = [num]
                groups[num] = size
            maxSize = max(maxSize, size)
        return maxSize
