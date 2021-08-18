a, b = map(int, input().split())
c, d = map(int, input().split())
r = set()
now = b

while now < d:
    now += a

d %= c
while True:
    if now % c == d:
        print(now)
        return

    if (now % c) in r:
        print(-1)
        return

    r.add(now % c)

    now += a
