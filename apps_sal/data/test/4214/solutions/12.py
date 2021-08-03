import itertools

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy_d = [[0] * N for _ in range(N)]
xylist = list(itertools.permutations([n for n in range(N)], N))

for i in range(N - 1):
    for h in range(i + 1, N):
        xy_d[i][h] = ((xy[i][0] - xy[h][0])**2 + (xy[i][1] - xy[h][1])**2)**.5
        xy_d[h][i] = ((xy[i][0] - xy[h][0])**2 + (xy[i][1] - xy[h][1])**2)**.5

ans = 0

# print(xy_d)

for g in range(len(xylist)):
    for t in range(N - 1):
        # print(xy_d[xylist[g][t]][xylist[g][t+1]])
        ans += xy_d[xylist[g][t]][xylist[g][t + 1]]

print(ans / len(xylist))
