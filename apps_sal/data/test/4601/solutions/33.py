n,k = map(int,input().split())
h = list(map(int,input().split()))
h.sort(reverse = True)
if n < k:
    k = n
ans = 0
for i in range(k):
    h[i] = 0
for i in range(n):
    ans += h[i]
print(ans)
