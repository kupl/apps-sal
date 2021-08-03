class Solution:
    def longestPrefix(self, strn: str) -> str:
        max_prefs = [0] * len(strn)

        curr = 0
        for idx in range(1, len(strn)):
            while True:
                if curr == 0:
                    if strn[idx] == strn[0]:
                        curr = 1
                    max_prefs[idx] = curr
                    break
                else:
                    if strn[idx] == strn[curr]:
                        curr += 1
                        max_prefs[idx] = curr
                        break
                    else:
                        curr = max_prefs[curr - 1]

        return strn[:max_prefs[-1]]
