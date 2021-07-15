n, m = list(map(int, input().split()))
a = []
for i in range(m):
    a.append(int(input()))

mod = 1000000007

memo = [-1]*(n+1)
memo[0] = 0

for k in range(m):
    memo[a[k]] = 0

for i in range(1, n+1):
    if memo[i] != -1:
        pass 
    elif i <= 2:
        memo[i] = memo[i-1] + 1
    else:
        memo[i] = memo[i-1] + memo[i-2]
print(memo[-1]%mod)
