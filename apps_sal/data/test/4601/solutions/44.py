n, k = map(int, input().split())
h = list(map(int,input().split()))
ans = 0

h = sorted(h,reverse=True)

for i in range(k,n):
    ans += h[i]

print(ans)
