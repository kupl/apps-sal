class Solution:
    def largestComponentSize(self, A):
        if not A:
            return 0

        def findAndCompact(l, i):  # require i >= 0
            if l[i] == i:
                return i
            p = l[i]
            if p >= 0 and l[p] == p:
                return p
            while p >= 0 and l[p] != p:
                p = l[p]
            root = p

            # compact
            p = i
            while p >= 0 and l[p] != p:
                t = l[p]
                l[p] = root
                p = t
            return root

        slist = [-1] * len(A)
        d = {}  # record prime->(root of union-find set)
        for i in range(len(A)):
            n = A[i]
            has_factor = False
            for j in range(2, int(sqrt(n)) + 1):
                if n % j == 0:
                    has_factor = True
                    k = n // j
                    #print(n, j, k)
                    ri = -1 if slist[i] < 0 else findAndCompact(slist, slist[i])
                    rj = -1 if j not in d else findAndCompact(slist, d[j])
                    rk = -1 if k not in d else findAndCompact(slist, d[k])
                    if ri < 0 and rj < 0 and rk < 0:
                        slist[i] = d[j] = d[k] = i
                    else:
                        mm = min([item for item in (ri, rj, rk) if item >= 0])
                        if slist[i] >= 0:
                            slist[ri] = mm
                        if j in d:
                            slist[rj] = mm
                        if k in d:
                            slist[rk] = mm
                        slist[i] = d[j] = d[k] = mm
            if not has_factor:  # prime
                if A[i] not in d:
                    slist[i] = d[A[i]] = i
                else:
                    slist[i] = d[A[i]]
            #print(slist, d)

        for i in range(len(A)):
            findAndCompact(slist, i)
        # print('### ', slist)
        cc = Counter(slist)
        m = cc.most_common(1)
        return m[0][1]
