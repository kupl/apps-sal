class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = [1] * 5
        b = [1] * 5
        for i in range(1, n):
            b[0] = a[1]
            b[1] = a[0] + a[2]
            b[2] = a[0] + a[1] + a[3] + a[4]
            b[3] = a[2] + a[4]
            b[4] = a[0]
            a = b.copy()

        return sum(b) % (10**9 + 7)
