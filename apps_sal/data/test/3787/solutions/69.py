(n, a, b) = map(int, input().split())
if a * b < n:
    print(-1)
elif a + b - 1 > n:
    print(-1)
else:
    if a * b == n:
        l = [b] * a
    else:
        l = [b] * ((n - a) // (b - 1)) + [(n - a) % (b - 1) + 1] + [1] * (a - 1 - (n - a) // (b - 1))
    j = 0
    c = 0
    ans = [0] * n
    for i in l:
        c += i
        for k in range(c, c - i, -1):
            ans[j] = k
            j += 1
    print(' '.join(map(str, ans)))
