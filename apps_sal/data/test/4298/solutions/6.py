# 入力を受ける
N, D = map(int, input().split())

# 監視員は、2*D+1本みれる
k = 2 * D + 1

# 出力する
print(N // k if N % k == 0 else (N // k) + 1)
