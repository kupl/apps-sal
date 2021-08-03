N = int(input())
xu = []
for i in range(N):
    xu.append(list(map(str, input().split())))
a = 0
for i in range(N):
    if xu[i][1] == 'JPY':
        a += float(xu[i][0])
    if xu[i][1] == 'BTC':
        a += float(xu[i][0]) * (380000.0)
print(a)
