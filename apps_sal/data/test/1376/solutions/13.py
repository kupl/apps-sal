n = int(input())
ai = list(map(int,input().split()))
ans = 0
dists = [[0,0] for i in range(n+1)]
dists[0][1] = 1
dists[0][0] = 1
j = 1
for i in ai:
    if dists[i][0] == 0:
        dists[i][0] = j
    else:
        dists[i][1] = j
    j += 1
for i in range(n):
    ans += min(abs(dists[i][0] - dists[i+1][0]) + abs(dists[i][1] - dists[i+1][1]),
               abs(dists[i][1] - dists[i+1][0]) + abs(dists[i][0] - dists[i+1][1]) )
print(ans)

