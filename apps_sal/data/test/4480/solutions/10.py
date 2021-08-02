class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        prefixSumMap = defaultdict(list)
        sumUpto = {}
        total = 0
        for i in range(len(A)):
            prefixSumMap[total].append(i)
            total += A[i]
            sumUpto[i] = total
        s = 0
        for i in range(len(A) - 1, 1, -1):
            s += A[i]
            target = total - 2 * s
            if prefixSumMap.get(target) != None:
                for j in prefixSumMap[target]:
                    if j < i and j > 0 and sumUpto[j - 1] == s:
                        return True
        return False
