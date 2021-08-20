class Solution:

    def hammingWeight(self, n: int) -> int:
        suma = 0
        while n != 0:
            suma += 1
            print(n, n - 1)
            n &= n - 1
        return suma
