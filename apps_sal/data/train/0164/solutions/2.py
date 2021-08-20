class Solution:

    def minInteger(self, num: str, k: int) -> str:
        rest = num
        move = 0
        s = ''
        for dig in range(10):
            count = 0
            digC = str(dig)
            for (i, c) in enumerate(rest):
                if c == digC:
                    if k < move + i - count:
                        rest = rest.replace(digC, '', count)
                        s += digC * count
                        remain = k - move
                        mid = rest[0:remain + 1]
                        while remain:
                            tmp = min(mid)
                            for (ti, tc) in enumerate(mid):
                                if tc == tmp:
                                    remain -= ti
                                    s += tc
                                    rest = rest.replace(tc, '', 1)
                                    mid = rest[0:remain + 1]
                                    break
                        return s + rest
                    move += i - count
                    count += 1
            rest = rest.replace(digC, '')
            s += digC * count
        return s
