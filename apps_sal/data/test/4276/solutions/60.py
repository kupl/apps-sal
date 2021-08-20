(n, T) = list(map(int, input().split()))
l = []
count = 0
for i in range(0, n):
    (c, t) = list(map(int, input().split()))
    if t < T or t == T:
        l.append(c)
    else:
        count += 1
if len(l) == 0:
    print('TLE')
else:
    print(int(min(l)))
