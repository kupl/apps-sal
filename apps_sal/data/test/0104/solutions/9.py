n = int(input())
a = list(map(int, input().split()))
sum1 = sum(a)
so = 0
for i in range(n):
    so += a[i]
    if(so >= sum1 / 2):
        ans = i
        break
print(ans + 1)
