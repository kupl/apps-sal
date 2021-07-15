n, k = map(int, input().split())
ans = 0

if k == 0:
    print(n*n)
    return

# mod b ということは、あまり0~b-1が n // b回つづく
for b in range(k, n+1):
    x = n // b
    y = n % b
    ans += (b-k) * x
    if y >= k:
        ans += y + 1 - k
print(ans)
