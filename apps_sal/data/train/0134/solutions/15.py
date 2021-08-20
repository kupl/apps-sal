def parcfact(m):
    return sum([fact(m1) for m1 in range(1, m)])


def fact(m):
    p = 1
    for ii in range(m):
        p = p * min(9, 10 - ii)
    return p


class Solution:

    def numDupDigitsAtMostN(self, N: int) -> int:
        found = {}
        NS = str(N)
        res = parcfact(len(NS))
        found = {}

        def count(par):
            res = 0
            if len(par) == len(NS) and par <= NS:
                return 1
            elif len(par) < len(NS):
                for ii in range(10):
                    if par.find(str(ii)) < 0 and par + str(ii) <= NS[:len(par) + 1]:
                        if par + str(ii) < NS[:len(par) + 1]:
                            if not len(par) in found:
                                found[len(par)] = count(par + str(ii))
                            res = res + found[len(par)]
                        else:
                            res = res + count(par + str(ii))
            return res
        for ii in range(1, int(NS[0]) + 1):
            res = res + count(str(ii))
        return N - res
