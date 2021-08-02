def gcd(x, y):
    if y == 0:
        return x

    r = x % y
    return gcd(y, r)


A, B, C, D = [int(x) for x in input().split()]
if C > D:
    E = C * D // gcd(C, D)
else:
    E = C * D // gcd(D, C)

divC = B // C - (A - 1) // C
divD = B // D - (A - 1) // D
divE = B // E - (A - 1) // E
div = divC + divD - divE
ans = B - A + 1 - div

print(ans)
