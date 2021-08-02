n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
r = 0
xy = [0] * n
for ii in range(n):
    xy[ii] = v[ii] - c[ii]
    if xy[ii] < 0:
        xy[ii] = 0
print(sum(xy))
