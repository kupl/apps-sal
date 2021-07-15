from bisect import bisect_left
n, *l = list(map(int, open(0).read().split()))
l.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ng = n - bisect_left(l, l[i] + l[j]) + 1
        ans += (n - j) - ng
print(ans)

