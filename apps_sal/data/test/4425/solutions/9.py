(n, k) = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    num = i
    p = 1 / n
    if num >= k:
        ans += p
        continue
    while num < k:
        num = num * 2
        p = p * (1 / 2)
    ans += p
print(ans)
