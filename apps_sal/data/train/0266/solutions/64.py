class Solution:
    def numSplits(self, s: str) -> int:
        fila = {}
        tot = len(set(s))

        x = set()
        for i in range(len(s)):
            x.add(s[i])
            if len(x) == tot:
                fa = i
                break

        x = set()
        for i in range(len(s) - 1, -1, -1):
            x.add(s[i])
            if len(x) == tot:
                la = i
                break

        if fa <= la:
            return la - fa

        for i, c in enumerate(s):
            if c not in fila:
                fila[c] = [i, i]
            else:
                fila[c][1] = i
        firsts, lasts = set(), set()
        for a, b in fila.values():
            firsts.add(a)
            lasts.add(b)
        ret = 0
        cl, cr = 0, len(fila)
        for i in range(len(s) - 1):
            if i in firsts:
                cl += 1
            if i in lasts:
                cr -= 1
            ret += int(cl == cr)
            if cr < cl:
                break
        return ret
