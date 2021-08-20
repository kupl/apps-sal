(N, K, *A) = map(int, open(0).read().split())
A.sort(reverse=True)
cur = 0
ans = 0
for a in A:
    if cur + a < K:
        cur += a
        ans += 1
    else:
        ans = 0
print(ans)
