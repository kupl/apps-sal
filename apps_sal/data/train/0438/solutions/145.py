class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        vals = [0 for _ in range(len(arr)+2)]
        numGroups = 0
        res = -1
        for p in range(len(arr)):
            i = arr[p]
            if vals[i-1] == 0 and vals[i+1] == 0:
                vals[i] = 1
                if m == 1:
                    numGroups += 1
            else:
                if vals[i-1] == 0:
                    groupStart = i
                else:
                    groupStart = i - vals[i-1]
                    if vals[i-1] == m:
                        numGroups -= 1
                if vals[i+1] == 0:
                    groupEnd = i
                else:
                    groupEnd = i + vals[i+1]
                    if vals[i+1] == m:
                        numGroups -= 1
                groupLength = groupEnd - groupStart + 1
                vals[groupStart] = vals[groupEnd] = groupLength
                if groupLength == m:
                    numGroups += 1
            if numGroups > 0:
                res = p + 1
        return res
