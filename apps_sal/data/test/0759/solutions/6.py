hh, mm = list(map(int, input().split()))
curminutes = hh * 60 + mm

h, d, c, n = list(map(int, input().split()))

cost_now = ((h + n - 1) // n) * c

thenminutes = 20 * 60
if thenminutes <= curminutes:
    print(cost_now * 0.8)
else:
    hunger_then = (thenminutes - curminutes) * d + h
    # print('now', cost_now)
    print(min(cost_now, (hunger_then + n - 1) // n * c * 0.8))
