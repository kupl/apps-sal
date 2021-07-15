n = int(input())
a = list(map(int, input().split()))
maxi = 10**11
ans = 0
for i in range(n - 1, -1, -1):
    maxi = max(min(a[i], maxi - 1), 0)
    ans += maxi
print(ans)

