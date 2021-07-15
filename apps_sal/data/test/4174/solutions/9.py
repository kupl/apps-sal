n, x = list(map(int,input().split()))
l = list(map(int,input().split()))
a = [0]
for i in range(n):
    tmp = a[i] + l[i]
    a.append(tmp)
ans = 0
for i in range(n + 1):
    if (a[i] <= x):
        ans = ans + 1

print(ans)

