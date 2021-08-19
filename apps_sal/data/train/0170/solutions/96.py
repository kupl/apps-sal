class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == sorted(arr):
            return 0
        L = len(arr)

        left = [arr[0]]
        right = [arr[-1]]

        for i in range(1, L):
            if arr[i] >= left[-1]:
                left += [arr[i]]
            else:
                break

        for i in range(L - 2, -1, -1):
            if arr[i] <= right[0]:
                right.insert(0, arr[i])
            else:
                break

        while len(left) - 1 >= L - len(right) and left[-1] == right[0]:
            left.pop(-1)
        print((left, right, L))

        ret = 0
        arr_len = 0
        for i in range(len(left)):
            for j in range(len(right)):
                temp = 0
                if left[i] <= right[j]:
                    temp = i + 1 + len(right) - j
                    break
            # if left[i] in right:
            #     idx_right = right.index(left[i])
            #     temp = i+1+len(right)-idx_right
            # else:
            #     idx_right = len(right)-1
            #     temp = 0
            arr_len = max(arr_len, temp)

        return L - max(len(left), len(right), arr_len)
