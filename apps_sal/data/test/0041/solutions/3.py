n = int(input())
a = list(map(int, input().split()))

ans = [n for _ in range(n)]
tmp = n
for i in range(n):
    if a[i] == 0:
        tmp = 0
    else:
        tmp += 1
    ans[i] = min(ans[i], tmp)

tmp = n
for i in range(n - 1, -1 , -1):
    if a[i] == 0:
        tmp = 0
    else:
        tmp += 1
    ans[i] = min(ans[i], tmp)

print(' '.join(map(str, ans)))


