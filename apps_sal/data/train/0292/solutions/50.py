class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        c1 = [-9999999999999, -9999999999999, -1]
        c2 = [-9999999999999, -9999999999999, -1]
        c3 = [-9999999999999, -9999999999999, -1]
        c4 = [-9999999999999, -9999999999999, -1]
        c5 = [-9999999999999, -9999999999999, -1]
        c6 = [-9999999999999, -9999999999999, -1]
        c7 = [-9999999999999, -9999999999999, -1]
        c8 = [-9999999999999, -9999999999999, -1]

        lim = len(arr1)

        for i in range(0, lim):
            if arr1[i] + arr2[i] + i > c1[0]:
                c1[0] = arr1[i] + arr2[i] + i
                c1[2] = i

            if arr1[i] - arr2[i] + i > c2[0]:
                c2[0] = arr1[i] - arr2[i] + i
                c2[2] = i

            if -arr1[i] - arr2[i] + i > c3[0]:
                c3[0] = -arr1[i] - arr2[i] + i
                c3[2] = i

            if -arr1[i] + arr2[i] + i > c4[0]:
                c4[0] = -arr1[i] + arr2[i] + i
                c4[2] = i

            if arr1[i] + arr2[i] - i > c5[0]:
                c5[0] = arr1[i] + arr2[i] - i
                c5[2] = i

            if arr1[i] - arr2[i] - i > c6[0]:
                c6[0] = arr1[i] - arr2[i] - i
                c6[2] = i

            if -arr1[i] - arr2[i] - i > c7[0]:
                c7[0] = -arr1[i] - arr2[i] - i
                c7[2] = i

            if -arr1[i] + arr2[i] - i > c8[0]:
                c8[0] = -arr1[i] + arr2[i] - i
                c8[2] = i
        for i in range(0, lim):
            if -arr1[i] - arr2[i] - i > c1[1] and i != c1[2]:
                c1[1] = -arr1[i] - arr2[i] - i

            if -arr1[i] + arr2[i] - i > c2[1] and i != c2[2]:
                c2[1] = -arr1[i] + arr2[i] - i

            if arr1[i] + arr2[i] - i > c3[1] and i != c3[2]:
                c3[1] = arr1[i] + arr2[i] - i

            if arr1[i] - arr2[i] - i > c4[1] and i != c4[2]:
                c4[1] = arr1[i] - arr2[i] - i

            if -arr1[i] - arr2[i] + i > c5[1] and i != c5[2]:
                c5[1] = -arr1[i] - arr2[i] + i

            if -arr1[i] + arr2[i] + i > c6[1] and i != c6[2]:
                c6[1] = -arr1[i] + arr2[i] + i

            if arr1[i] + arr2[i] + i > c7[1] and i != c7[2]:
                c7[1] = arr1[i] + arr2[i] + i

            if arr1[i] - arr2[i] + i > c8[1] and i != c8[2]:
                c8[1] = arr1[i] - arr2[i] + i

        v1 = 0
        if -9999999999999 not in c1:
            v1 = c1[0] + c1[1]
        v2 = 0
        if -9999999999999 not in c2:
            v2 = c2[0] + c2[1]
        v3 = 0
        if -9999999999999 not in c3:
            v3 = c3[0] + c3[1]
        v4 = 0
        if -9999999999999 not in c4:
            v4 = c4[0] + c4[1]
        v5 = 0
        if -9999999999999 not in c5:
            v5 = c5[0] + c5[1]
        v6 = 0
        if -9999999999999 not in c6:
            v6 = c6[0] + c6[1]
        v7 = 0
        if -9999999999999 not in c7:
            v7 = c7[0] + c7[1]
        v8 = 0
        if -9999999999999 not in c8:
            v8 = c8[0] + c8[1]

        print((v1, v2, v3, v4, v5, v6, v7, v8))
        return max(v1, v2, v3, v4, v5, v6, v7, v8)
