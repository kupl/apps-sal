class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        states = [None] * len(arr)
        numSizeM = 0
        latestM = -1
        for i in range(len(arr)):
            ind = arr[i] - 1
            if ind != 0 and ind != len(arr) - 1 and states[ind - 1] != None and states[ind + 1] != None:
                leftInd = ind - states[ind - 1][0]
                rightInd = ind + states[ind + 1][1]
                if states[leftInd][1] == m:
                    numSizeM -= 1
                if states[rightInd][0] == m:
                    numSizeM -= 1
                groupSize = states[leftInd][1] + 1 + states[rightInd][0]
                states[leftInd][1] = groupSize
                states[rightInd][0] = groupSize
                if groupSize == m:
                    numSizeM += 1
            elif ind != 0 and states[ind - 1] != None:
                leftInd = ind - states[ind - 1][0]
                if states[leftInd][1] == m:
                    numSizeM -= 1
                groupSize = states[leftInd][1] + 1
                states[leftInd][1] = groupSize
                states[ind] = [groupSize, 1]
                if groupSize == m:
                    numSizeM += 1
            elif ind != len(arr) - 1 and states[ind + 1] != None:
                rightInd = ind + states[ind + 1][1]
                if states[rightInd][0] == m:
                    numSizeM -= 1
                groupSize = states[rightInd][0] + 1
                states[rightInd][0] = groupSize
                states[ind] = [1, groupSize]
                if groupSize == m:
                    numSizeM += 1
            else:
                states[ind] = [1, 1]
                if m == 1:
                    numSizeM += 1
            if numSizeM > 0:
                latestM = i + 1
        return latestM
