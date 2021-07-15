maxx = -1
minn = 10**10
bad = []
a = int(input())
for i in range(a):
    x, y = list(map(int, input().split(' ')))
    bad.append([x, y])
    maxx = max(maxx, y)
    minn = min(minn, x)

for i in range(a):
    if bad[i][0] <= minn <= maxx <= bad[i][1]:
        print(i+1)
        quit()
print(-1)

