n, k = map(int, input().split())
# a+b=xの組み合わせの数を管理する配列
P = [0 for _ in range(2 * n + 1)]

if k < 0:
    k = -k
for x in range(1, 2 * n + 1):
    P[x] = min(x - 1, 2 * n + 1 - x)

ans = 0
for i in range(k + 2, 2 * n + 1):
    ans += P[i] * P[i - k]
print(ans)
