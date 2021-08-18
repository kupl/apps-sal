class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        possible = dict()
        for winSize in range(minSize, maxSize + 1):
            for winI in range(len(s) - winSize + 1):
                win = s[winI: winI + winSize]
                letters = set(win)
                if len(letters) <= maxLetters:
                    if win in possible:
                        possible[win] += 1
                    else:
                        possible[win] = 1
        if possible:
            return max(possible.values())
        else:
            return 0
