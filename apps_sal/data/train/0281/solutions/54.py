class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return 0
        aux = dict()
        for i in range(len(s)):
            if s[i] != t[i]:
                val1, val2 = ord(s[i]), ord(t[i])
                if val1 < val2:
                    if val2 - val1 in aux:
                        aux[val2 - val1] += 1
                    else:
                        aux[val2 - val1] = 1
                else:
                    if 26 - val1 + val2 in aux:
                        aux[26 - val1 + val2] += 1
                    else:
                        aux[26 - val1 + val2] = 1
        ans = 0
        for elem in aux:
            ans = max(ans, 26 * (aux[elem] - 1) + elem)
        return ans <= k
