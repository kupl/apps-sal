def f(t, k):
    (i, j) = (0, 1)
    (s, d) = (0, t[0])
    n = len(t)
    while j <= n:
        if d > k:
            d -= t[i]
            i += 1
        elif d == k:
            if t[i] and (j == n or t[j]):
                s += 1
            else:
                (a, b) = (i - 1, j - 1)
                while j < n and t[j] == 0:
                    j += 1
                while t[i] == 0:
                    i += 1
                s += (i - a) * (j - b)
            if j < n:
                d += t[j]
            d -= t[i]
            i += 1
            j += 1
        else:
            if j < n:
                d += t[j]
            j += 1
    return s


(s, n) = (0, int(input()))
t = list(map(int, input()))
if n:
    k = sum(t)
    if k == 0:
        print(0)
    else:
        p = [(i, n // i) for i in range(max(1, n // k), int(n ** 0.5) + 1) if n % i == 0]
        for (a, b) in p:
            if a != b:
                s += 2 * f(t, a) * f(t, b)
            else:
                k = f(t, a)
                s += k * k
        print(s)
else:
    n = len(t)
    m = n * (n + 1)
    s = j = 0
    while j < n:
        if t[j] == 0:
            i = j
            j += 1
            while j < n and t[j] == 0:
                j += 1
            k = (j - i) * (j - i + 1) // 2
            s += k
        j += 1
    print((m - s) * s)
