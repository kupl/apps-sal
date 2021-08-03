class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        options = []
        options = self.recursiveSplit(s)
        bestcount = 0
        for option in options:
            count = 0
            encountered = {}
            valid = True
            for substr in option:
                if substr not in encountered:
                    encountered[substr] = 1
                    count += 1
                else:
                    valid = False
                    break
            if valid and count > bestcount:
                bestcount = count
        return bestcount

    def recursiveSplit(self, s: str) -> str:
        if len(s) == 1:
            return [[s]]
        elif len(s) == 0:
            return [[]]
        options = []
        for i in range(0, len(s)):
            recursiveOptions = self.recursiveSplit(s[:i])
            for option in recursiveOptions:
                newoption = option.copy()
                newoption.append(s[i:])
                options.append(newoption)
        return options
