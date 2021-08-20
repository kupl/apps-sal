class Solution:

    def minOperations(self, n):
        arr = []
        count = 0
        for x in range(n):
            arr.append(2 * x + 1)
        avg = sum(arr) // n
        for x in range(n):
            count += abs(arr[x] - avg)
        return count // 2


sol = Solution()
x = sol.minOperations(3)
print(x)
