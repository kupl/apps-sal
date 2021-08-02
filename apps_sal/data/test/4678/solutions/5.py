n = int(input())
a = list(map(int, input().split()))
tmp = a[0]
ans = 0
for i in range(1, n):
    if tmp > a[i]:
        ans += tmp - a[i]
    else:
        tmp = a[i]
print(ans)
