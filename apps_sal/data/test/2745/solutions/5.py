class Solution:

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        (m, n, k, result, wordbase) = (len(s), len(words), len(words[0]), [], {})
        for value in words:
            if value in wordbase:
                wordbase[value] += 1
            else:
                wordbase[value] = 1
        for i in range(min(k, m - k * n + 1)):
            (base, starts, startw) = ({}, i, i)
            while starts + k * n <= m:
                temp = s[startw:startw + k]
                startw += k
                if temp not in wordbase:
                    starts = startw
                    base.clear()
                else:
                    if temp in base:
                        base[temp] += 1
                    else:
                        base[temp] = 1
                    while base[temp] > wordbase[temp]:
                        base[s[starts:starts + k]] -= 1
                        starts += k
                    if startw - starts == k * n:
                        result.append(starts)
        return result
