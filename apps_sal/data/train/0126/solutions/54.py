class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        validWords = {}
        for i in range(0, len(s)):
            for j in range(i + minSize - 1, min(i + maxSize, len(s))):
                ss = s[i:j + 1]
                if len(set(ss)) <= maxLetters:
                    if ss in validWords:
                        validWords[ss] += 1
                    else:
                        validWords[ss] = 1

        if validWords:
            all_values = validWords.values()
            return max(all_values)
        else:
            return 0
