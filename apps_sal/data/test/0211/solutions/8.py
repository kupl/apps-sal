d = 1000000009
n, m, k = map(int, input().split())
if (n - m) * k > n: print(m)
else:
    t = n // k - n + m + 1
    print(((pow(2, t, d) - 1 - t) * k + m) % d)
