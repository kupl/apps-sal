n = int(input())
spectator = 3
for _ in range(n):
    cur = int(input())
    if cur == spectator:
        print('NO')
        break
    spectator = {1, 2, 3}.difference({spectator, cur}).pop()
else:
    print('YES')


