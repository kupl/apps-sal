class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        L1 = [arr[0]]
        L2 = []

        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                L1.append(arr[i])
            else:
                break
        temp = [arr[-1]]
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                temp.append(arr[i])
            else:
                break
        L2 = temp[-1::-1]

        margin = len(arr) - (len(L1) + len(L2))
        m = min(len(L1), len(L2))

        MIN = m + margin
        LENGTH1 = len(L1) - 1
        LENGTH2 = len(L2) - 1
        # print(L1,L2)

        i = len(L1) - 1
        j = len(L2) - 1

        while i >= 0 and j >= 0:
            if L1[i] <= L2[j]:
                j -= 1

                a = LENGTH1 - i
                b = j + 1
                # print(i,j,a+b)
                MIN = min(MIN, margin + a + b)

            else:
                i -= 1
                if j != LENGTH2:
                    j += 1
                # print(i,j)
        # print()
        i = 0
        j = 0
        while i < len(L1) and j < len(L2):
            if L1[i] <= L2[j]:
                i += 1
                a = LENGTH1 - i + 1
                b = j
                # print(i,j,a+b)
                MIN = min(MIN, margin + a + b)

            else:
                j += 1
                if i != 0:
                    i -= 1
                # print(i,j)

        if MIN < 0:
            MIN = 0
        return MIN
