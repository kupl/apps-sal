n = int(input())
l = list(map(int, input().split()))
l.sort()
f = 0
for i in range(n - 1):
    if f == 0:
        l[i], l[i + 1] = l[i + 1], l[i]
        f = 1
    else:
        f = 0
ans = (n - 1) // 2
print(ans)
print(*l)
