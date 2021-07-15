n = int(input())
a =  list(map(int, input().split()))

total = 0
for i in range(n):
    total += a[i]*(1 if i%2==0 else -1)

ans = [total]

for i in range(0, n-1):
    ans.append(2*a[i]-ans[i])

print(" ".join(map(str, ans)))
