def f(b, n):
    if n < b:
        return n
    else:
        (q, r) = divmod(n, b)
        return f(b, q) + r


n = int(input())
s = int(input())
if n == s:
    print(n + 1)
else:
    b = 2
    while b * b <= n:
        if f(b, n) == s:
            print(b)
            break
        b += 1
    else:
        p = 1
        ans = 10 ** 13
        while p * p <= n:
            b = (n - s) // p + 1
            if p < b and s - p < b and (f(b, n) == s):
                ans = min(ans, b)
            p += 1
        if ans == 10 ** 13:
            print(-1)
        else:
            print(ans)
