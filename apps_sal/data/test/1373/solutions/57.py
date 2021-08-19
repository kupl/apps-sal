n, k = list(map(int, input().split()))
mod = 10 ** 9 + 7

ans = 0

for p in range(k, n + 2):
    minimum = p * (p - 1) // 2  # 0〜(p-1)の和
    maximum = p * (2 * n - p + 1) // 2  # (n-p+1)〜nの和
    ans += maximum - minimum + 1
    ans %= mod

print(ans)
