from fractions import gcd


def nok(a, b):
    return a * b // gcd(a, b)


(x, y, a, b) = list(map(int, input().split()))
lcs = nok(x, y)
l = lcs - a % lcs + a if a % lcs != 0 else a
ans = (b - l) // lcs + 1
print(ans)
