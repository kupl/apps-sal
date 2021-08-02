n, l = list(map(int, input().split()))
S = n * l + (n * (n + 1)) // 2 - n
pd = S + 1
for x in range(1, n + 1):
    d = - l - x + 1
    if pd > abs(d):
        ans = S + d
    pd = d

print(ans)
