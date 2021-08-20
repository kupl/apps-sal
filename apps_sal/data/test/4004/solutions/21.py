n = int(input())
arr = list(map(int, input().strip().split()))
arr = sorted(arr)
ans = 10000000000
for k in range(200):
    d = -1
    fl = 0
    for i in range(n):
        c = abs(arr[i] - k)
        if d == -1:
            d = c
        elif d != c and c > 0:
            fl = 1
    if fl == 0:
        ans = min(ans, d)
if ans == 10000000000:
    print(-1)
else:
    print(ans)
