class Solution:
    def getIndex(self, val, arr):
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid][0] < val:
                start = mid + 1
            else:
                end = mid
        if arr[start][0] < val:
            start += 1
        return start

    def oddEvenJumps(self, A: List[int]) -> int:
        items = len(A)
        even = [False] * items
        odd = [False] * items
        goodindex = 1
        even[-1], odd[-1] = True, True
        vals = [[A[-1], items - 1]]

        for index in range(items - 2, -1, -1):
            insind = self.getIndex(A[index], vals)

            if insind < len(vals):
                eind = vals[insind][1]
                odd[index] = even[eind]

            eq = False
            if insind < len(vals) and vals[insind][0] == A[index]:
                oind = vals[insind][1]
                even[index] = odd[oind]
                eq = True
            elif insind > 0:
                oind = vals[insind - 1][1]
                even[index] = odd[oind]

            if eq:
                vals[insind][1] = index
            else:
                vals.insert(insind, [A[index], index])
            if odd[index]:
                goodindex += 1
        return goodindex
