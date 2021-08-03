from sys import maxsize as m
from itertools import product as P


class Solution:
    def bazinga(self, N, p):
        pass


def __starting_point():
    n, b = list(map(int, input().split(' ')))
    ct, pt, lpt, cb = 0, 0, [], 0
    result = []
    for i in range(n):
        ti, di = list(map(int, input().split()))
        # print(pt,lpt,'--',ti,di,cb)
        res = 0
        if pt == 0:
            pt += ti + di
            lpt += [pt]
            res = pt
        else:
            if ti < lpt[0]:
                if cb < b:
                    pt += di
                    lpt += [pt]
                    res = pt
                    cb += 1
                elif cb >= b:
                    res = -1

            elif ti >= lpt[0]:
                # print(lpt,pt,ti,di)
                if ti > lpt[-1]:
                    pt += abs(lpt[-1] - ti) + di
                else:
                    pt += di
                lpt += [pt]
                res = pt
                cb += 1
                while ti >= lpt[0]:
                    if len(lpt) == 1:
                        break
                    lpt.pop(0)
                    if cb > 0:
                        cb -= 1

        result += (str(res),)
    print(' '.join(result))


__starting_point()
