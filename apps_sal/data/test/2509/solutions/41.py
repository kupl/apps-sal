n, k = list(map(int, input().split()))
ans = 0
for b in range(k + 1, n + 1):
    res = (n - k) % b
    quo = (n - k) // b
    if b - k - 1 > res:
        # ans+=(res+1)*(quo+1)+(b-k-res-1)*quo
        ans += (b - k) * quo + res + 1
    else:
        ans += (b - k) * (quo + 1)
    ans -= (k == 0)

print(ans)

# n-k-j>=b*r  j=0,...,b-k-1
