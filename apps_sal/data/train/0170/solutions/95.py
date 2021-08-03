class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if not arr:
            return 0
        a, temp = [], []
        temp.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] >= 0:
                temp.append(arr[i])
            else:
                a.append(temp)
                temp = []
                temp.append(arr[i])
        if temp:
            a.append(temp)
        if len(a) <= 1:
            return 0
        else:
            deletelen = []
            a0, a_1 = a[0], a[-1]
            deletelen.append(len(arr) - len(a0))
            deletelen.append(len(arr) - len(a_1))
            if a0[-1] <= a_1[0]:
                deletelen.append(len(arr) - len(a0) - len(a_1))
            else:
                for i in range(len(a_1)):
                    for j in range(len(a0) - 1, -1, -1):
                        if a_1[i] >= a0[j]:
                            deletelen.append(len(arr) - len(a0) - len(a_1) + i + (len(a0) - j - 1))
                            break
            return min(deletelen)
