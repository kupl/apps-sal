n, d = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
ans = 2
for i in range(1, n):
    if(a[i] - a[i - 1] - 2 * d > 0):
        ans += 2
    elif(a[i] - a[i - 1] - 2 * d == 0):
        ans += 1
print(ans)
