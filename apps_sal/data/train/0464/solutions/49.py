class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            count = 0
            i = 1
            while i < n:
                print(i)
                count += n - i
                i += 2
            return count
