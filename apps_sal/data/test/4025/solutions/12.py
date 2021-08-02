d = [0, 1, 2, 0, 2, 1, 0]

a, b, c = [int(item) for item in input().split()]

ans = -float("inf")

k = min(a // 3, b // 2, c // 2)
g = k * 7
a -= 3 * k
b -= 2 * k
c -= 2 * k

for s in range(7):
    days = 0
    ca, cb, cc = a, b, c
    for day in range(s, s + 7):
        if d[day % 7] == 0:
            if ca == 0:
                break
            ca -= 1
        elif d[day % 7] == 1:
            if cb == 0:
                break
            cb -= 1
        else:
            if cc == 0:
                break
            cc -= 1
        days += 1

    ans = max(ans, days)


print(ans + g)
