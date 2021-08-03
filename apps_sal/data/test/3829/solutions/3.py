m, n = list(map(int, input().split()))

P = 1
ans = 0

while(m > 0):
    p = P * (1 - (((m - 1) / m)**n))
    ans += m * p
    m -= 1
    P -= p
print(ans)
