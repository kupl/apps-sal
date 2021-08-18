import bisect
n = int(input())
a = sorted(list(map(int, input().split(" "))))
ans = 0
for i in range(1, n - 1):
    b = a[:i]
    c = a[i + 1:]
    for j in b:
        ans += bisect.bisect(c, a[i] + j - 0.1)
print(ans)
