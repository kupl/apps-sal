import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = 0
ind = -1
for i in range(n):
    tmp = a[i]
    l = i
    r = i
    max_height = a[i]
    for j in range(0, l)[::-1]:
        if a[j] >= max_height:
            tmp += max_height
        else:
            tmp += a[j]
            max_height = a[j]
    max_height = a[i]
    for j in range(r + 1, n):
        if a[j] >= max_height:
            tmp += max_height
        else:
            tmp += a[j]
            max_height = a[j]
    if ans < tmp:
        ans = tmp
        ind = i
i = ind
ans = [0] * n
tmp = a[i]
l = i
r = i
max_height = a[i]
ans[i] = a[i]
for j in range(0, l)[::-1]:
    if a[j] >= max_height:
        tmp += max_height
    else:
        tmp += a[j]
        max_height = a[j]
    ans[j] = max_height
max_height = a[i]
for j in range(r + 1, n):
    if a[j] >= max_height:
        tmp += max_height
    else:
        tmp += a[j]
        max_height = a[j]
    ans[j] = max_height
print(*ans)
