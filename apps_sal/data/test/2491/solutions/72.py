n, m = list(map(int, input().split()))
# from, to, cost
edges = [list(map(int, input().split())) for _ in range(m)]

score = [-float('inf')] * (n+1)
score[1] = 0
cnt = 0

for i in range(n):
    for frm, to, cost in edges:
        if score[to] < score[frm] + cost:
            if i == n - 1 and to == n:
                print('inf')
                return
            score[to] = score[frm] + cost

print((score[n]))

