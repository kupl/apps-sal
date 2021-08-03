n, k = list(map(int, input().split(" ")))
thing = input()
thing = thing.split(" ")
balls = []
for t in thing:
    balls += [int(t)]

if n <= k:
    m = max(balls)
else:
    squeeze = n - k

    m = 0

    for i in range(squeeze):
        current = balls[i] + balls[2 * squeeze - 1 - i]
        m = max(current, m)

    m = max(balls[n - 1], m)

print(m)
