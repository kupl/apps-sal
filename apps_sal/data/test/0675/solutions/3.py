m, t, r = map(int, input().split())
data = list(map(int, input().split()))

if r > t:
    print(-1)
else:
    candles = []
    total = 0

    for x in data:
        while candles and candles[0] + t - 1 < x:
            candles.pop(0)

        need = r - len(candles)

        for n in range(need):
            candles.append(x - (need - 1) + n)
            total += 1

    print(total)
