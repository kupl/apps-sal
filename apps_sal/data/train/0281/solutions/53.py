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
        print(cda)
        del cda[0]
        elements = sorted(list(cda.items()), key=lambda x: (x[1], x[0]), reverse=True)
        minK = 0
        try:
            key = elements[0]
            minK = (key[1] - 1) * 26 + key[0]
        except IndexError:
            pass
        print(minK)
        return k >= minK
