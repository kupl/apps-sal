class Solution:
    def findRow(self, matrix, target, l, h):
        if l > h:
            return -1

        elif l == h:
            return h

        mid = l + int((h - l) / 2)

        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid
        elif matrix[l][0] <= target < matrix[mid][0]:
            return self.findRow(matrix, target, l, mid - 1)
        else:
            return self.findRow(matrix, target, mid + 1, h)

    def bSearch(self, arr, target, l, h):
        if l > h:
            return -1

        mid = l + int((h - l) / 2)

        if arr[mid] == target:
            return mid
        elif arr[l] <= target < arr[mid]:
            return self.bSearch(arr, target, l, mid - 1)
        else:
            return self.bSearch(arr, target, mid + 1, h)

    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        inRow = self.findRow(matrix, target, 0, rows - 1)
        print(('row present in %s' % inRow))
        arr = matrix[inRow]

        index = self.bSearch(arr, target, 0, cols - 1)
        print(('present at index %s' % index))

        if index != -1:
            return True

        return False
