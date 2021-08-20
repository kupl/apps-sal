(n, t) = map(int, input().split())
y = 10 ** 5
c = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    if c[i][1] <= t:
        y = min(y, c[i][0])
if y != 10 ** 5:
    print(y)
else:
    print('TLE')
