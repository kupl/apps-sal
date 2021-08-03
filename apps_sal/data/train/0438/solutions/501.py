from sortedcontainers import SortedDict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        a = [0] * n
        for i in arr:
            a[i - 1] = 1
        last = -1
        lastcnt = 0
        parentcnts = SortedDict()
        for i, val in enumerate(a):
            if val == 1:
                if i == 0 or a[i - 1] == 0:
                    last = i
                    lastcnt = 0
                    parentcnts[i] = 0
                lastcnt += 1
                parentcnts[last] += 1
        for key in parentcnts:
            if parentcnts[key] == m:
                return n

        for x in range(n - 1, -1, -1):
            # print(parentcnts)
            ind = arr[x] - 1
            leftone, rightone = True, True
            if ind == 0 or a[ind - 1] == 0:
                leftone = False
            if ind == n - 1 or a[ind + 1] == 0:
                rightone = False
            if not leftone and not rightone:
                parentcnts.pop(ind)
                continue
            if not leftone:
                parentcnts[ind + 1] = parentcnts[ind] - 1
                parentcnts.pop(ind)
                if m == parentcnts[ind + 1]:
                    return x
                continue

            ins_ind = parentcnts.peekitem(parentcnts.bisect_right(ind) - 1)[0]
            if not rightone:
                parentcnts[ins_ind] -= 1
                if m == parentcnts[ins_ind]:
                    return x
                continue

            parentcnts[ind + 1] = parentcnts[ins_ind] - (ind - ins_ind + 1)
            parentcnts[ins_ind] = ind - ins_ind
            if m == parentcnts[ind + 1] or m == parentcnts[ins_ind]:
                return x
        return -1
