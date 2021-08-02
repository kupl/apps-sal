n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort()
for i in range(n - 1):
    if a[i + 1][1] < a[i][1]:
        print('Happy Alex')
        return
print('Poor Alex')
