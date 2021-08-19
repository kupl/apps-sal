n = int(input())
spot = [0] + list(map(int, input().split())) + [0]
plst = [0] * n
dissum = 0
for i in range(1, n + 1):
    plst[i - 1] = abs(spot[i + 1] - spot[i - 1]) - (abs(spot[i + 1] - spot[i]) + abs(spot[i] - spot[i - 1]))
    dissum += abs(spot[i] - spot[i - 1])
dissum += abs(spot[n])
for i in range(n):
    print(dissum + plst[i])
