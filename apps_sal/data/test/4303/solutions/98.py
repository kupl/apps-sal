n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = 10**10
for left in range(n-k+1):
    right = left+k-1
    ans = min(ans, abs(x[left])+abs(x[right]-x[left]), abs(x[right])+abs(x[right]-x[left]))
print(ans)
