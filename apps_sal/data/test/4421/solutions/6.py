n, k = list(map(int, input().split()))
d = list(map(int, input().split()))
di = dict()
for i in range(n):
    if d[i] % k in di:
        di[d[i] % k] += 1
    else:
        di[d[i] % k] = 1
ans = 0
if 0 in di:
    ans = di[0] // 2
for i in range(1, k // 2 + 1):
    if i in di and k - i in di:
        if i == k - i:
            ans += di[i] // 2
        else:
            ans += min(di[i], di[k - i])
print(ans * 2)
