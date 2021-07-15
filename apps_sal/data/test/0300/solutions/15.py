def go():
    n = int(input())
    a = sorted([int(i) for i in input().split(' ')])
    s = sum(a)
    if s / n >= 4.5:
        return 0
    c = 0
    for i in range(n):
        s -= a[i]
        a[i] = 5
        s += 5
        c += 1
        if s / n >= 4.5:
            return c
print(go())

