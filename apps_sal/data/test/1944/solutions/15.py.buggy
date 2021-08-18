import sys
n = int(input())
v = []
for i in range(n):
    v.append(list(map(int, input().split())))
v.sort()
for i in range(n - 1):
    if v[i + 1][1] < v[i][1]:
        print('Happy Alex')
        return
print('Poor Alex')
