N = int(input())
ans = N
for i in range(N + 1):
    n = i
    m = N - i
    res = 0
    nine = 1
    while nine * 9 <= n:
        nine *= 9
    while nine != 1:
        res += n // nine
        n %= nine
        nine /= 9
    res += n
    six = 1
    while six * 6 <= m:
        six *= 6
    while six != 1:
        res += m // six
        m %= six
        six /= 6
    res += m
    ans = min(ans, int(res))
print(ans)
