class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        lim = len(arr)
        pref = [arr[0]]
        d = dict()
        e = dict()
        d[arr[0]] = [0]
        e[arr[0]] = 1
        for i in range(1, lim):
            pref.append(pref[-1] + arr[i])
            try:
                d[pref[-1]].append(i)
                e[pref[i]] += 1
            except:
                d[pref[-1]] = [i]
                e[pref[i]] = 1
        A = [lim] * lim
        for i in range(0, lim):
            val = target + pref[i] - arr[i]
            if val in d:
                l = 0
                h = e[val] - 1
                mn = lim + 1
                while l <= h:
                    m = (l + h) // 2
                    if d[val][m] >= i:
                        if d[val][m] < mn:
                            mn = d[val][m]
                        h = m - 1
                    else:
                        l = m + 1
                if mn != lim + 1:
                    A[i] = mn - i + 1
            if arr[i] == target:
                A[i] = 1
        pmn = lim
        p = [lim] * lim
        s = [lim] * lim
        for i in range(0, lim):
            if i + A[i] < lim and p[i + A[i]] > A[i]:
                p[i + A[i]] = A[i]
        smn = lim
        if A[-1] < lim:
            smn = A[-1]
        for i in range(lim - 1, -1, -1):
            if A[i] < smn:
                smn = A[i]
            s[i] = smn
        mn = lim + 1
        for i in range(0, lim):
            if p[i] + s[i] < mn:
                mn = p[i] + s[i]
        if mn >= lim + 1:
            return -1
        return mn
