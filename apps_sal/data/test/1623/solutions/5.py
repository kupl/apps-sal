(n, l, r) = [int(i) for i in input().split()]
ans = n - l
for i in range(l):
    ans += 2 ** i
print(ans, end=' ')
ans = 2 ** (r - 1) * (n - r)
for i in range(r):
    ans += 2 ** i
print(ans)
