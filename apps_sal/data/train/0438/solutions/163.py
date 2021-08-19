class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        mc = 0
        step = -1
        tuples = {}
        for i in range(len(arr)):
            pos = arr[i]
            (minPos, maxPos) = (pos, pos)
            if pos - 1 in tuples:
                minPos = tuples[pos - 1][0]
                if tuples[pos - 1][1] - minPos + 1 == m:
                    mc -= 1
                    if mc == 0:
                        step = i
            if pos + 1 in tuples:
                maxPos = tuples[pos + 1][1]
                if maxPos - tuples[pos + 1][0] + 1 == m:
                    mc -= 1
                    if mc == 0:
                        step = i
            tuples[minPos] = (minPos, maxPos)
            tuples[maxPos] = tuples[minPos]
            if maxPos - minPos + 1 == m:
                mc += 1
        if mc > 0:
            step = len(arr)
        return step
