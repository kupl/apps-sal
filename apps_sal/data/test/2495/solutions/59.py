n = int(input())
a = list(map(int, input().split()))

ans1 = 0
ans2 = 0

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += a[i]
    sum2 += a[i]
    if sum1*(-1)**i>=0:
        ans1 += abs(sum1)+1
        sum1 = -(-1)**i
    if sum2*(-1)**i<=0:
        ans2 += abs(sum2)+1
        sum2 = (-1)**i

print((min(ans1,ans2)))

