n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
if k == 1:
    print(min(a))
elif k == 2:
    b = [a[0]] * (n - 1)
    for i in range(1, n - 1):
        b[i] = min(b[i - 1], a[i])
    c = [a[n - 1]] * (n - 1)
    for i in range(n - 3, -1, -1):
        c[i] = min(c[i + 1], a[i + 1])
    ans = - 10 ** 10
    for i in range(n - 1):
        ans = max(ans, max(b[i], c[i]))
    print(ans)
else:
    print(max(a))
