n, m, d = map(int, input().split())
p = list(map(int, input().split()))

positions = [0] * len(p)
positions[-1] = n + 1 - p[-1]
for i in reversed(range(len(p)-1)):
    positions[i] = positions[i+1] - p[i]

def feasible(p, positions, d):
    if positions[0] > d:
        return False
    for i in range(1, len(p)):
        if positions[i] - (positions[i-1] + p[i-1] - 1) > d:
            return False
    if n+1 - (positions[-1] + p[-1] - 1) > d:
        return False
    return True

g = [0] * m
g[0] = d
for i in range(1, m):
    g[i] = g[i-1] + p[i-1] - 1 + d

i = 0
while not feasible(p, positions, d) and i < len(p):
    positions[i] = g[i]
    i += 1

if feasible(p, positions, d):
    print("YES")
    board = [0] * n
    for i in range(m):
        for j in range(p[i]):
            board[positions[i]-1+j] = i+1
    for e in board:
        print(e, end=' ')
    print()
else:
    print("NO")
