n = int(input())

a_tmp = list(map(int, input().split()))
a = []
for i in range(n):
    a.append([a_tmp[i], i + 1])
a.sort(key=lambda x: x[0])

for i in range(n):
    print(a[i][1], end=" ")
