n, a, b, c, t = list(map(int, input().split()))
messages = list(map(int, input().split()))

if b < c:
    money = n * a
    for m in messages:
        money += (t - m) * (c - b)
else:
    money = n * a

print(money)

