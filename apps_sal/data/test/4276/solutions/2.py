(n, T) = map(int, input().split())
x = list()
cnt = 0
for i in range(n):
    (c, t) = map(int, input().split())
    if t <= T:
        x.append(c)
        cnt = 1
if cnt == 0:
    print('TLE')
else:
    print(min(x))
