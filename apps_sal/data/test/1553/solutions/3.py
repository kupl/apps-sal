def f(a):
    a.sort()
    ans = 0
    for i in range(len(a) - 1, -1, -2):
        ans += a[i]
    return ans


(n, h) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    b = a[:i].copy()
    x = f(b)
    if x <= h:
        ans = i
print(ans)
