class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ADict = {}
        A = sorted(A)
        print(A)
        for a in A:
            if a in ADict:
                ADict[a] += 1
            else:
                ADict[a] = 1
        ijSame = False
        keys = sorted(ADict)
        totWays = 0
        for i in range(len(keys)):
            if keys[i] > target:
                break
            elif ADict[keys[i]] < 3:
                continue
            elif keys[i] * 3 == target:
                numOcc = ADict[keys[i]]
                totWays += numOcc * (numOcc - 1) * (numOcc - 2) / 6

        if len(keys) == 1:
            return int(totWays % (10**9 + 7))
        for i in range(len(keys)):
            if keys[i] > target:
                break
            elif ADict[keys[i]] < 2:
                continue
            else:
                sum = keys[i] * 2
                remain = target - sum
                if (not(remain == keys[i]) and remain in keys):
                    numDoubleOcc = ADict[keys[i]]
                    numSingleOcc = ADict[remain]
                    totWays += numDoubleOcc * (numDoubleOcc - 1) / 2 * numSingleOcc
        if len(keys) == 2:
            return int(totWays % (10**9 + 7))
        for i in range(len(keys)):
            if keys[i] > target:
                break
            for j in range(i + 1, len(keys)):
                sum = keys[i] + keys[j]
                if sum > target:
                    break
                remaining = target - sum
                if remaining in keys[j + 1:]:
                    totWays += ADict[keys[i]] * ADict[keys[j]] * ADict[remaining]

        return int(totWays % (10**9 + 7))
