3

n, t = tuple(map(int, input().split()))
a = list(map(int, input().split()))
s = 0
ans = 0
i = 0
for j in range(n):
    s += a[j]
    while s > t:
        s -= a[i]
        i += 1
    ans = max(ans, j - i + 1)
print(ans)

