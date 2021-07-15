n = int(input())
rows = []
rows.append(list(map(int, input().split())))
rows.append(list(map(int, input().split())))
best = [0, 0]
nextBest = [0, 0]
for k in range(n):
    nextBest[0] = max(best[1] + rows[0][k], best[0])
    nextBest[1] = max(best[0] + rows[1][k], best[1])
    best[0] = nextBest[0]
    best[1] = nextBest[1]
print(max(best))

