btc = 380000
N = int(input())
ans = 0
for i in range(N):
    (x, u) = input().split()
    if u == 'JPY':
        ans += float(x)
    else:
        ans += float(x) * btc
print(ans)
