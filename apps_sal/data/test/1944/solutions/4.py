n = int(input())
c = [[]] * n
for i in range(n):
    c[i] = [int(j) for j in input().split()]
c.sort()
for i in range(n - 1):
    if c[i][0] < c[i + 1][0] and c[i][1] > c[i + 1][1]:
        print('Happy Alex')
        return
print('Poor Alex')

