(n, k, p) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 1000000000000000
ans = int(ans)
for i in range(k - n + 1):
    tmp = 0
    for j in range(n):
        tmp = max(tmp, abs(a[j] - b[i + j]) + abs(b[i + j] - p))
    ans = min(ans, tmp)
print(ans)
