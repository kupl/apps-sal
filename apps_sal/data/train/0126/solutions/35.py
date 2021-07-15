class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sub = dict()

        for i in range(len(s) - minSize + 1):
            d = dict()
            for k in range(i, i + minSize):
                if s[k] in d:
                    d[s[k]] += 1
                else:
                    d[s[k]] = 1

            if len(d) <= maxLetters:
                phrase = s[i:i+minSize]
                if phrase in sub:
                    sub[phrase] += 1
                else:
                    sub[phrase] = 1
            else:
                continue

            for j in range(i + minSize, i + maxSize):
                if j < len(s):
                    if len(d) <= maxLetters:
                        phrase = s[i:j+1]
                        if phrase in sub:
                            sub[phrase] += 1
                        else:
                            sub[phrase] = 1
                    else:
                        break

                    if s[j] in d:
                        d[s[j]] += 1
                    else:
                        d[s[j]] = 1

        if not sub:
            return 0
        return max(sub.values())
