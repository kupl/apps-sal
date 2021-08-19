(n, m) = list(map(int, input().split()))
a = set(list((int(input()) for _ in range(m))))
mod = 1000000007
memo = [0] * (n + 1)
memo[0] = 1
for i in range(1, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]
    if i in a:
        memo[i] = 0
print(memo[-1] % mod)
