class Solution:

    def sumSubseqWidths(self, a: List[int]) -> int:
        a.sort()
        print(a)
        count = 0
        n = 1
        c = a[0]
        for (m, i) in enumerate(a[1:]):
            n *= 2
            count += (n - 1) * i - c
            c = c * 2 + i
        return count % (pow(10, 9) + 7)
