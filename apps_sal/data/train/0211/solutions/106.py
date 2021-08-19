class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        if len(d) == len(s):
            return len(d)

        def waysToSplit(s):  # return list of sequences
            if not s:
                return []
            if len(s) == 1:
                return [[s]]
            else:
                res = []
                for i in range(len(s)):
                    first = [s[:i + 1]]
                    second = waysToSplit(s[i + 1:])
                    for seq in second:
                        res.append(first + seq)
                res.append([s])
            return res

        maxCount = 1

        sequences = waysToSplit(s)
        # print(sequences)
        for seq in sequences:
            s = set()
            count = 0
            foundDup = False
            for element in seq:
                if element in s:
                    foundDup = True
                    break
                else:
                    count += 1
                    s.add(element)
            if not foundDup:
                maxCount = max(maxCount, count)
        return maxCount
