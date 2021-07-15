n, k = map(int, input().split())
p = list(map(int, input().split()))

a = [1+(i-1)/2 for i in p]
l = sum(a[:k])
ans = l
for i in range(1, n-k+1):
    l = l-a[i-1]+a[k+i-1]
    ans = max(ans, l)
print(ans)
