def f(x, v, n):
    a, p, s = 0, 0, 1
    c = [0] * n + [1] + [0] * n
    for i in v:
        if(i < x):
            p += 1
            s += c[p + n]
        else:
            s -= c[p + n]
            p -= 1
        c[p + n] += 1
        a += s
    return a


n, x = list(map(int, input().split()))
v = [int(i) for i in input().split()]
print(f(x + 1, v, n) - f(x, v, n))
