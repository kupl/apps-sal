from collections import Counter


class Solution:
    def findLatestStep(self, arr1: List[int], m: int) -> int:
        if m == len(arr1):
            return len(arr1)

        def find(arr, i):
            if i == arr[i]:
                return i
            arr[i] = find(arr, arr[i])
            return arr[i]

        def union(arr, i, j, c, mCount):
            u = find(arr, i)
            v = find(arr, j)
            if u != v and v in c and c[v] == m:
                mCount -= 1
            if u != v and u in c and c[u] == m:
                mCount -= 1
            if u != v:
                arr[v] = u
            return u, mCount

        ret = -1
        t = [0] * len(arr1)
        par = [i for i in range(len(arr1))]
        c = dict()
        mCount = 0
        for i in range(len(arr1)):
            pri = arr1[i] - 1
            t[pri] = 1
            p1, p2 = arr1[i] - 2, arr1[i]
            if(p1 < 0 or not t[p1]) and (p2 >= len(arr1) or not t[p2]):
                c[pri] = 1
                if c[pri] == m:
                    mCount += 1
            if p1 >= 0 and t[p1]:
                u, mCount = union(par, p1, pri, c, mCount)
                c[u] += 1
                if u in c and c[u] == m:
                    mCount += 1
            if p2 < len(arr1) and p1 >= 0 and t[p1] and t[p2]:
                u, mCount = union(par, p1, p2, c, mCount)
                c[u] += c[p2]
                if u in c and c[u] == m:
                    mCount += 1
                del c[p2]
            elif p2 < len(arr1) and t[p2]:
                u, mCount = union(par, pri, p2, c, mCount)
                c[pri] = c[p2] + 1
                if pri in c and c[pri] == m:
                    mCount += 1
                del c[p2]
            if mCount:
                ret = i + 1
        return ret
