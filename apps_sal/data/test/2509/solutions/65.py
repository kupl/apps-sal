n,k = map(int, open(0).read().split())

ans = 0

for b in range(k+1, n+1):
    c = n//b*(b-k)
    if k:
        d = max(0, n%b-k+1)
    else:
        d = n%b
    ans += c
    ans += d

print(ans)
