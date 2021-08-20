def cmp(a):
    return a[0]


(n, d) = [int(x) for x in input().split()]
arr = []
for i in range(n):
    l = [int(x) for x in input().split()]
    arr.append(l)
arr.sort(key=cmp)
i = 0
ans = arr[0][1]
now = arr[0][1]
for j in range(1, n):
    if arr[j][0] - arr[i][0] < d:
        now += arr[j][1]
    else:
        if now > ans:
            ans = now
        while arr[j][0] - arr[i][0] >= d:
            now -= arr[i][1]
            i += 1
        now += arr[j][1]
if now > ans:
    ans = now
print(ans)
