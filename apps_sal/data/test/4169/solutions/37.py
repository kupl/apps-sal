n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab = sorted(ab)

money = 0
for i in ab:
    money += i[0] * min(m, i[1])
    m -= min(m, i[1])

    if m <= 0:
        break

print(money)
