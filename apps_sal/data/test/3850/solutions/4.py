def read():
    return [int(x) for x in input().split()]


n, k, p = read()
a = read()
b = read()
a.sort()
b.sort()
ans = 2e9 + 1
ans = int(ans)
for i in range(k - n + 1):
    tmp = 0
    for j in range(n):
        tmp = max(tmp, abs(a[j] - b[i + j]) + abs(b[i + j] - p))
    ans = min(ans, tmp)
print(ans)
