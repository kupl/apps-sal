n = int(input())
games = list(map(int, input().split()))
strike = [0] * n
for i in range(n):
    strike[i] = 1
    for j in range(i):
        if games[j] <= games[i]:
            strike[i] = max(strike[i], strike[j] + 1)
print(max(strike))
