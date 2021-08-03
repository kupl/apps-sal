n, t = list(map(int, input().split()))
li = [list(map(int, input().split())) for i in range(n)]

lis = []
for i in li:
    if i[1] <= t:
        lis.append(i[0])
if len(lis) == 0:
    print('TLE')
else:
    print((min(lis)))
