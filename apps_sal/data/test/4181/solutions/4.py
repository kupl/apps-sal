
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = sum(a)
for i in range(n):
    if a[i]>=b[i]:
        a[i] -= b[i]
    else:
        a[i+1] = max(0,a[i+1]-b[i]+a[i])
        a[i] = 0
print((ans-sum(a)))

