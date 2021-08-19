# 街の数はn+1個　aiはi番目の街を襲うモンスター
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for x in range(n):
    if a[x] >= b[x]:
        count += b[x]
    if a[x] < b[x]:
        count += a[x]
        if b[x] - a[x] <= a[x + 1]:
            count += b[x] - a[x]
            a[x + 1] = a[x + 1] - (b[x] - a[x])
        else:
            count += a[x + 1]
            a[x + 1] = 0


print(count)
