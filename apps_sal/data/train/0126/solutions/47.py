class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sol = {}
        for i in range(len(s) - minSize + 1):
            count = {}
            length = 0
            for j in range(minSize - 1):
                length += 1
                c = s[i+j]
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
            while length < maxSize and (i + length) < len(s):
                c = s[i + length]
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
                if len(count) <= maxLetters:
                    substring = s[i: i+length+1]
                    if substring in sol:
                        sol[substring] += 1
                    else:
                        sol[substring] = 1
                length += 1
        maximum = 0
        for substring in sol:
            if sol[substring] > maximum:
                maximum = sol[substring]
        return maximum
