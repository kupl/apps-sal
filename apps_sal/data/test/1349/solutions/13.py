def read():
    return list(map(int, input().split()))


T = int(input())
for ____ in range(T):
    r = 0
    (n, k) = read()
    a = [1] * n
    b = list(read())
    i = 0
    while sum(a):
        for _ in b:
            _ -= 1
            if _ - i >= 0:
                a[_ - i] = 0
            if _ + i < n:
                a[_ + i] = 0
        i += 1
        r += 1
    print(r)
