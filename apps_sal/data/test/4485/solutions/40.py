n, m = list(map(int, input().split()))
ab  = list(list(map(int, input().split())) for _ in range(m))

goal = [0] * n
start = [0] * n

for a, b in ab:
    if a == 1:
        start[b] = 1
    if b == n:
        goal[a] = 1

flg = False
for i in range(n):
    if start[i] and goal[i]:
        flg = True

print(('POSSIBLE' if flg else 'IMPOSSIBLE'))

