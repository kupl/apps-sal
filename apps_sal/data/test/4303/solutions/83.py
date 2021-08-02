n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")
for i in range(n - k + 1):
    # 0の位置から移動し、i〜i+kまでのろうそくに火をつけた場合の移動時間について左右で確認し、最小を求める
    l = abs(x[i]) + abs(x[i] - x[i + k - 1])
    r = abs(x[i + k - 1]) + abs(x[i] - x[i + k - 1])
    ans = min(ans, l, r)
print(ans)
