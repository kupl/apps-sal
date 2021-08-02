n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if a[i] - a[i + 1] > ans:
        ans = a[i] - a[i + 1]
ans = ans - m
if(ans < 0):
    ans = 0
print(ans)
