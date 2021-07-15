n = int(input())
s = list(map(int, input().split()))
max_games = 0
for i in range(n+1):
    max_games = max(max_games, s[:i].count(0) + s[i:].count(1))
print(max_games)

