n = int(input())
l = list(map(int, input().split()))
f = [0] * n
k = 0
ans = 0
while k < n:
    for i in range(n):
        if f[i] == 0 and l[i] <= k:
            k += 1
            f[i] = 1
    if k == n:
        break
    ans += 1
    for i in range(n):
        if f[n - i - 1] == 0 and l[n - i - 1] <= k:
            k += 1
            f[n - i - 1] = 1
    if k == n:
        break
    ans += 1
print(ans)
