class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        s, lastOcc, countsDict, n = [0] * (len(arr) + 1), -1, defaultdict(int), len(arr)
        for traversei, ind in enumerate(arr):
            i = ind - 1
            newSize = s[i - 1] + s[i + 1] + 1
            countsDict[s[i + 1]] -= 1
            countsDict[s[i - 1]] -= 1
            countsDict[newSize] += 1
            s[i - s[i - 1]] = s[i + s[i + 1]] = newSize
            if countsDict[m] > 0:
                lastOcc = traversei + 1
        return lastOcc
