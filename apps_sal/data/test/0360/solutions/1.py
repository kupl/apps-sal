n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
k = int(input())
ans = n
for i in range(n):
    if k > a[i][1]:
        ans -= 1
print(ans)

