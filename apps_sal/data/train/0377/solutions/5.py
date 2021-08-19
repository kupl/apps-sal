class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        # H.C.F of A and B
        x, y = min(A, B), max(A, B)
        print(x, y)
        hcf = x

        while (y % hcf != 0 or x % hcf != 0) and hcf > 1:
            hcf -= 1
        print(hcf)
        gcd = int(x * y / hcf)
        print(gcd)
        start, end = x, N * x
        while start <= end:
            mid = start + int((end - start) / 2)
            count = int(mid / x) + int(mid / y) - int(mid / gcd)
            if count == N:
                break
            elif count > N:
                end = mid - 1
            else:
                start = mid + 1
        while mid % x != 0 and mid % y != 0:
            mid -= 1
        return mid % (10**9 + 7)
