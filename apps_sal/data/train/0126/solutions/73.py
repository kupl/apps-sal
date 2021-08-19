class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        toSearch = {}
        for size in range(minSize, maxSize + 1):
            for i in range(len(s) - size + 1):
                S = s[i:i + size]
                letters = len(set(S))
                if letters <= maxLetters:
                    if S in toSearch:
                        toSearch[S] += 1
                    else:
                        toSearch[S] = 1
        # print(toSearch)
        ans = 0
        for e in toSearch:
            ans = max(ans, toSearch[e])
        return ans
