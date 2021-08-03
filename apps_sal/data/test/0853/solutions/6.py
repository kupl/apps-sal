n = int(input())
d = dict()
d[5] = 0
d[0] = 0
a = list(map(int, input().split()))
for i in range(n):
    d[a[i]] += 1
d[5] -= d[5] % 9
if d[5] == 0 and d[0] == 0:
    print(-1)
elif d[5] == 0:
    print(0)
elif d[0] == 0:
    print(-1)
else:
    for i in range(d[5]):
        print(5, sep='', end='')
    for i in range(d[0]):
        print(0, sep='', end='')
