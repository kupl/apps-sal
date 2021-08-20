def delta(x):
    (l, r) = (-1, 100000)
    while l + 1 < r:
        mid = l + r >> 1
        tot = mid * (mid + 1) // 2
        if tot < x:
            l = mid
        else:
            r = mid
    if (r * (r + 1) // 2 - x) % 2 != 0:
        return r + 1 + r % 2
    else:
        return r


t = int(input())
for i in range(t):
    (a, b) = map(int, input().split())
    print(delta(abs(a - b)))
