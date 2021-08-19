class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        if len(s) == 1:
            return 1

        def splitter(str):
            for i in range(1, len(str)):
                start = str[0:i]
                end = str[i:]
                yield (start, end)
                for split in splitter(end):
                    result = [start]
                    result.extend(split)
                    yield result
        maxnum = 0
        for split in splitter(s):
            if len(set(split)) == len(split):
                maxnum = max(len(split), maxnum)
        if maxnum == 0:
            return self.maxUniqueSplit(s[:len(s) - 1])
        else:
            return maxnum
