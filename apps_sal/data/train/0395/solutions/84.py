class Solution:

    def findIndex(self, arr, val):
        if not arr:
            return 0
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
        n = len(A)
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        arr = [[A[-1], n - 1]]
        count = 1
        for index in range(n - 2, -1, -1):
            val = A[index]
            insindex = self.findIndex(arr, val)
            evenindex = None
            if insindex < len(arr):
                odd[index] = even[arr[insindex][1]]
                if arr[insindex][0] == val:
                    evenindex = arr[insindex][1]
                elif insindex > 0:
                    evenindex = arr[insindex - 1][1]
            else:
                evenindex = arr[insindex - 1][1]
            if evenindex is not None:
                even[index] = odd[evenindex]
            if insindex < len(arr) and arr[insindex][0] == val:
                arr[insindex][1] = index
            else:
                arr.insert(insindex, [val, index])
            if odd[index]:
                count += 1
        return count
