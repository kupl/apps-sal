from copy import copy


class Solution:

    def numSquarefulPerms(self, A: List[int]) -> int:
        d = dict()
        count = dict()
        lim = len(A)
        blank = dict()
        for i in range(0, lim - 1):
            try:
                count[A[i]] += 1
            except:
                blank[A[i]] = 0
                count[A[i]] = 1
            for j in range(i + 1, lim):
                if ((A[i] + A[j]) ** 0.5).is_integer():
                    try:
                        d[A[i]].add(A[j])
                    except:
                        d[A[i]] = set()
                        d[A[i]].add(A[j])
                    try:
                        d[A[j]].add(A[i])
                    except:
                        d[A[j]] = set()
                        d[A[j]].add(A[i])
        try:
            count[A[-1]] += 1
        except:
            count[A[-1]] = 1
            blank[A[-1]] = 0
        check = sorted(A)
        if d == dict():
            return 0
        f = set()
        c = 0

        def r(val, ld, l, lth):
            if lth == lim:
                f.add(tuple(l))
            elif val in d:
                for x in d[val]:
                    s = copy(ld)
                    if s[x] <= count[x]:
                        s[x] += 1
                        r(x, s, l + [x], lth + 1)
        for x in set(A):
            r(x, blank, [x], 1)
        for x in f:
            if sorted(list(x)) == check:
                c += 1
        return c
