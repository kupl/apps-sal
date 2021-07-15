n = int(input())
a = list(map(int,input().split()))
ans = 0
sum = 0
for i in range(n):
    sum += a[i]
    if sum*(-1)**i<=0:
        ans += abs(sum)+1
        sum = (-1)**i
ans2 = 0
sum = 0
for i in range(n):
    sum += a[i]
    if sum*(-1)**i>=0:
        ans2 += abs(sum)+1
        sum = -(-1)**i
print((min(ans,ans2)))

