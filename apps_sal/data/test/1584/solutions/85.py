import bisect
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n - 1):
    b = l[:i]
    c = l[i + 1:]
    for j in b:
        ans += bisect.bisect_left(c, l[i] + j)
print(ans)
