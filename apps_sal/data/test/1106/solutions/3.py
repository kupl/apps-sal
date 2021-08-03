def B():
    s = 0
    n = int(input())
    k = (1 << (n + 1)) - 1
    a = [0, 0] + list(map(int, input().split()))
    for i in range(k, 1, -2):
        u, v = a[i], a[i - 1]
        if u > v:
            u, v = v, u
        s += v - u
        a[i >> 1] += v
    return s


print(B())
