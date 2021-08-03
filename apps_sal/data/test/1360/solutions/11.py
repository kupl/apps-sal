n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort()
ans = a[0][1]
for i in range(n):
    if ans > a[i][1]:
        ans = a[i][0]
    else:
        ans = a[i][1]
print(ans)
