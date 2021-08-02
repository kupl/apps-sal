n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
for i in range(n):
    if a[i][1] >= k:
        print(n - i)
        break
