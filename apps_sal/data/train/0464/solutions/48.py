class Solution:
    def minOperations(self, n: int) -> int:
        A = [x * 2 + 1 for x in range(n)]
        s = sum(A) / n
        c = 0
        while True:
            for i in A:
                if i >= s:
                    return int(c)
                c += (s - i)
