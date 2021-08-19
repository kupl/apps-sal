(n, m, d) = map(int, input().split())
a = list(map(int, input().split()))
id = {a[i]: i for i in range(n)}
a.sort()


def Solve(x):
    for i in range(x, n):
        if a[i] - a[i - x] <= d:
            return False
    return True


l = 1
r = n
while l < r:
    mid = int((l + r) / 2)
    if Solve(mid):
        r = mid
    else:
        l = mid + 1
ans = [0 for i in range(n)]
for i in range(n):
    ans[id[a[i]]] = i % l + 1
print(l)
print(' '.join(map(str, ans)))
