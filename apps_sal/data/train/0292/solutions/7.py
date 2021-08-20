class Solution:

    def join(self, a: List[int], b: List[int], add=True, ascend=True):
        arr = []
        for i in range(len(a)):
            if add:
                arr.append(a[i] + b[i])
            else:
                arr.append(a[i] - b[i])
            if ascend:
                arr[i] += i
            else:
                arr[i] -= i
        return arr

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        if not len(arr1):
            return 0
        (mins, maxes) = ([], [])
        idx = []
        for (i, arr) in enumerate([self.join(arr1, arr2, add, asc) for (add, asc) in [(True, True), (True, False), (False, True), (False, False)]]):
            mins.append(arr[0])
            maxes.append(arr[0])
            idx.append((0, 0))
            for j in range(1, len(arr)):
                if arr[j] < mins[i]:
                    mins[i] = arr[j]
                    idx[i] = (j, idx[i][1])
                if arr[j] > maxes[i]:
                    maxes[i] = arr[j]
                    idx[i] = (idx[i][0], j)
        largest_diff = float('-inf')
        if (arr1[idx[0][0]] > arr1[idx[0][1]]) == (arr2[idx[0][0]] > arr2[idx[0][1]]) and idx[0][0] <= idx[0][1]:
            largest_diff = maxes[0] - mins[0]
        if (arr1[idx[1][0]] > arr1[idx[1][1]]) == (arr2[idx[1][0]] > arr2[idx[1][1]]) and idx[1][0] >= idx[1][1]:
            largest_diff = max(largest_diff, maxes[1] - mins[1])
        if (arr1[idx[2][0]] > arr1[idx[2][1]]) != (arr2[idx[2][0]] > arr2[idx[2][1]]) and idx[2][0] <= idx[2][1]:
            largest_diff = max(largest_diff, maxes[2] - mins[2])
        if (arr1[idx[3][0]] > arr1[idx[3][1]]) != (arr2[idx[3][0]] > arr2[idx[3][1]]) and idx[3][0] >= idx[3][1]:
            largest_diff = max(largest_diff, maxes[3] - mins[3])
        return largest_diff
