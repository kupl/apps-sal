class Solution:

    def minOperations(self, n: int) -> int:

        def isAllEqual(array):
            for i in range(len(array[1:])):
                if array[i] != array[0]:
                    return False
            return True
        arr = [2 * x + 1 for x in range(n)]
        count = 0
        x = 0
        y = len(arr) - 1
        while x < y:
            diff = int((arr[y] - arr[x]) / 2)
            arr[x] += diff
            arr[y] -= diff
            count += diff
            x += 1
            y -= 1
        return count
