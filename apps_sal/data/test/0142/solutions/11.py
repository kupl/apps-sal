n, L = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
for i in range(1, n):
    if (c[i] > c[i-1] * 2):
        c[i] = c[i-1] * 2
ans1 = 0
ans2 = 0
ans = 10**20
for i in range(n-1, -1, -1):
    r1 = L // (2**i)
    r2 = (L + 2**i - 1) // (2**i)
    L -= (r1 * 2**i)
    ans1 = ans2 + r2 * c[i]
    ans2 += r1 * c[i]
    ans = min(ans, ans1)
ans = min(ans, ans2)
print(ans)
