N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

money = 0
for a, b in AB:
    if M > b:
        money += a * b
        M -= b
    else:
        money += a * M
        break

print(money)
