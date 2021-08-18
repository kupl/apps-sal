import itertools
N = int(input())
x = []
y = []
for i in range(N):
    xy = list(map(int, input().split()))
    x.append(xy[0])
    y.append(xy[1])


l = [i for i in range(N)]
ans = 0
cnt = 0
for i in itertools.permutations(l, N):
    cnt += 1
    for j in range(1, N):
        x1 = x[i[j]]
        x2 = x[i[j - 1]]
        y1 = y[i[j]]
        y2 = y[i[j - 1]]
        ans += pow((x1 - x2)**2 + (y1 - y2)**2, 0.5)
ans /= cnt
print(ans)
