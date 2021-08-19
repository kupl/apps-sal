import pprint
n = int(input())
a = [[0] * 2 for i in range(n)]
memo = 0
ahozon = 0
for i in range(n):
    (a[i][0], a[i][1]) = map(int, input().split())
a.sort(key=lambda x: x[1])
for j in range(n):
    if memo <= 1:
        if a[j][1] - a[j][0] - ahozon >= 0:
            ahozon += a[j][0]
        else:
            memo += 1
if memo >= 1:
    print('No')
else:
    print('Yes')
