class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        r = 0
        o = 0
        a = 0
        k = 0

        frogs = 0
        max_frogs = 0
        for L in croakOfFrogs:

            if L == 'c':
                frogs += 1
                max_frogs = max(max_frogs, frogs)
                r += 1

            elif L == 'r':
                if r == 0:
                    return -1
                else:
                    r -= 1
                    o += 1

            elif L == 'o':
                if o == 0:
                    return -1
                else:
                    o -= 1
                    a += 1

            elif L == 'a':
                if a == 0:
                    return -1
                else:
                    a -= 1
                    k += 1

            else:
                if k == 0:
                    return -1
                else:
                    k -= 1
                    frogs -= 1

        if r + o + a + k != 0:
            return -1

        return max_frogs
