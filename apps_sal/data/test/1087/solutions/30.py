(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(41)[::-1]:
    S = sum(map(lambda x: x >> i & 1, a))
    if S > n // 2:
        m = 0
    else:
        m = 1 << i
    if S > n // 2 or m > k - cnt:
        ans += S << i
    else:
        ans += n - S << i
        cnt += m
print(ans)
