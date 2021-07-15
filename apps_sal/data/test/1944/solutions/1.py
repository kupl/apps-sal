__author__ = 'nikolay'
n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))
a.sort()
for i in range(1, n):
    if a[i][1] < a[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")

