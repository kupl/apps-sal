t = int(input())

for k in range(t):
    a, b, c = list(map(int, input().split()))

    d = [a, b, c]
    d.sort()
    a = 0

    if d[0] > 0:
        a += 1
        d[0] -= 1

    if d[1] > 0:
        a += 1
        d[1] -= 1

    if d[2] > 0:
        a += 1
        d[2] -= 1

    d.sort(reverse=True)

    if d[0] > 0 and d[1] > 0:
        a += 1
        d[0] -= 1
        d[1] -= 1

    if d[0] > 0 and d[2] > 0:
        a += 1
        d[0] -= 1
        d[2] -= 1

    if d[2] > 0 and d[1] > 0:
        a += 1
        d[2] -= 1
        d[1] -= 1

    if d[0] > 0 and d[1] > 0 and d[2] > 0:
        a += 1

    print(a)

