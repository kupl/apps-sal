n = int(input())
a = list(map(int, input().split()))
x = dict()
sum = 0
ans = n - 1
for i in range(n):
    sum += a[i]
    if sum in x:
        x[sum] += 1
    else:
        x[sum] = 1
    ans = min(ans, n - x[sum])
print(ans)
