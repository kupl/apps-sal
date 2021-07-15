n = int(input())
a = list(map(int,input().split()))
snuke = 0
arai = sum(a)
ans = 2*(10**9)
for i in range(n-1):
    snuke += a[i]
    arai -= a[i]
    ans = min(ans,abs(snuke-arai))
print(ans)
