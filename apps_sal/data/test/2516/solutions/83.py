(n, p) = map(int, input().split())
if p in (2, 5):
    c = 0
    for (i, x) in enumerate(map(int, input()[::-1])):
        if x % p == 0:
            c += n - i
    print(c)
else:
    c = [0] * p
    y = 0
    t = 1
    for x in map(int, input()[::-1]):
        y = (y + t * x) % p
        c[y] += 1
        t = 10 * t % p
    print(sum((i * (i - 1) // 2 for i in c)) + c[0])
