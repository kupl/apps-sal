n, m = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
ruiseki = [0] * (n + 1)
for i in range(n):
    ruiseki[i+1] = ruiseki[i] + a[i]
    
ans = [0] * n
for i in range(n):
    if i-m >=0:
        ans[i] = ruiseki[i+1] + ans[i-m]
    else:
        ans[i] = ruiseki[i+1] 
print(*ans)
