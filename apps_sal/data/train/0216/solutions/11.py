class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if not len(croakOfFrogs):
            return 0
        c = 0
        r = 0
        o = 0
        a = 0
        k = 0
        count = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                count += 1
                c += 1
            elif ch == 'r':
                if not c:
                    return -1
                c -= 1
                r += 1
            elif ch == 'o':
                if not r:
                    return -1
                r -= 1
                o += 1
            elif ch == 'a':
                if not o:
                    return -1
                o -= 1
                a += 1
            elif ch == 'k':
                if not a:
                    return -1
                a -= 1
                k = max(k, count)
                count -= 1
            else:
                return -1
        if not c and (not r) and (not o) and (not a):
            return k
        else:
            return -1
