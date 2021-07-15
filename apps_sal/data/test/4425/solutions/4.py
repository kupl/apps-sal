def p(n, k):
    if n >= k:
        return 1
    num = 0
    while n < k:
        n *= 2
        num += 1
    return 1 / 2 ** num

N, K = map(int, input().split())

ans = 0
for n in range(1, N + 1):
    ans += p(n, K)

ans /= N

print(ans)
