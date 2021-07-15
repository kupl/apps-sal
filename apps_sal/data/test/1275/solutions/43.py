n, k = map(int, input().split())
k = abs(k)
li = [0] * (n*2+1)
for i in range(2, n*2+1):
    li[i] = min(i-1, 2*n+1-i)
ans = 0
for i in range(k, n*2+1):
    ans += li[i]*li[i-k]
print(ans)
