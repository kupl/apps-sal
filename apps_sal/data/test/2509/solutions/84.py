n, k = map(int, input().split())

ans = 0
for b in range(1, n+1):
    loop = n//b
    ans += max(0, b-k)*loop + max(0, n%b-k+1)
if k==0:
    ans-=n
print(ans)
