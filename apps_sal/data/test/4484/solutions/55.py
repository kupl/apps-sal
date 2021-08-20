(n, m) = map(int, input().split())
if n < m:
    (n, m) = (m, n)
if m + 1 == n or m == n:
    if m + 1 == n:
        ans = 1
    else:
        ans = 2
    k = 1
    for i in range(1, n + 1):
        k *= i
        if i == m:
            ans *= k
        k = k % (10 ** 9 + 7)
    ans *= k
    print(ans % (10 ** 9 + 7))
else:
    print(0)
