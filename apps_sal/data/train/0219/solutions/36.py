import bisect


class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        starts = []
        startIndexes = []
        counts = [0] * len(hours)

        for i in range(len(hours)):
            if i > 0:
                counts[i] = counts[i - 1]
            if hours[i] > 8:
                counts[i] += 1
            else:
                counts[i] -= 1

        counts = [0] + counts

        for i in range(len(counts) - 1, -1, -1):
            numGood = counts[i]
            while starts and starts[-1] >= numGood:
                starts.pop()
                startIndexes.pop()

            starts.append(numGood)
            startIndexes.append(i)

        maxLen = 0
        for i, c in enumerate(counts):
            target = c - 1
            pos = bisect.bisect_right(starts, target)
            if pos == len(starts) or starts[pos] > target:
                pos -= 1
            if pos >= 0:
                lenHere = i - startIndexes[pos]
                maxLen = max(maxLen, lenHere)

        return maxLen
