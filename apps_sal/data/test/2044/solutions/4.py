(n, m) = map(int, input().split())
a = list(map(int, input().split()))
s = 0
ans = 0
for i in range(n):
    s += a[i]
    print(s // m - ans, end=' ')
    ans = s // m
