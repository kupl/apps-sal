import itertools
import math

N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
ave = 0
cnt = 0
for v in itertools.permutations([int(x) for x in range(N)], N):
    for i in range(1, len(v)):
        ave += math.sqrt((xy[v[i - 1]][0] - xy[v[i]][0])**2 + (xy[v[i - 1]][1] - xy[v[i]][1])**2)
    cnt += 1

ave = ave / cnt
print(ave)
