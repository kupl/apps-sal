import collections


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        n = n1

        diffArray = [(ord(t[i]) - ord(s[i])) % 26 for i in range(n)]

        cda = collections.Counter(diffArray)

        del cda[0]

        minK = 0
        if len(cda) > 0:
            key = max([(i[1], i[0])for i in list(cda.items())])
            minK = (key[0] - 1) * 26 + key[1]
        return k >= minK
