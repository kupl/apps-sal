n = int(input())
a = list(map(int, input().split()))

lsum = a[0]
rsum = sum(a[1:])
ans = abs(lsum - rsum)

for i in range(1, n - 1):
    lsum += a[i]
    rsum -= a[i]
    res = abs(lsum - rsum)

    if res < ans:
        ans = res

print(ans)
