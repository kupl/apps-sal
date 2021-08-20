(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
l = [int(input()) for i in range(m)]
ans = [0] * n
s = set()
for i in range(n - 1, -1, -1):
    s.add(a[i])
    ans[i] = len(s)
for i in range(m):
    print(ans[l[i] - 1])
