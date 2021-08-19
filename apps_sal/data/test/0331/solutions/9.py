(n, m, k) = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
ans = 10000000000
for i in range(n):
    if s[i] <= k and s[i]:
        ans = min(ans, 10 * abs(m - 1 - i))
print(ans)
