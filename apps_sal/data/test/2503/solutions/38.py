import numpy as np

N, K = map(int, input().split())
_3K = 3 * K
_2K = 2 * K
G = np.zeros((_2K, _3K), dtype='int64')  # 後から 2K * K に圧縮する
for _ in range(N):
    x, y, c = input().split()
    x, y = int(x), int(y)
    # 2K * 2K の黒の希望に置き換え
    if c == 'B':
        x = x % _2K
        y = y % _2K
    else:
        x = (x + K) % _2K
        y = y % _2K
    # さらに、 2K * K の黒の希望に圧縮する
    if (y >= K) and (x >= K):
        x -= K
        y -= K
    if (y >= K) and (x < K):
        x += K
        y -= K
    # 塗り方は右下がどのマスに来るかの 2K * K 通り
    # → 最終的に 2K * K のグリッドで表すことができる
    # 各希望を満たす塗り方は K * K 通り
    # → 2K * K のグリッド内の希望を満たす K * K マスに 1 を加算すれば、
    #   全希望の加算後には各マス＝各塗り方がいくつの希望を満たすかがわかる
    # K * K マスに 1 を加算するには o(K^2) かかってしまう
    # → いもす法を使う
    # 塗り方を 3K * 2K の範囲で考えて累積和をとった後、 2K * K の範囲に圧縮する
    G[y, x] += 1
    G[y + K, x + K] += 1
    G[y + K, x] -= 1
    G[y, x + K] -= 1

# 3K * 2K の範囲の累積和をとる
G = G.cumsum(axis=1).cumsum(axis=0)
# 2K * K の範囲に圧縮
G = G[:K, :_2K] + G[K:_2K, K:_3K] + np.concatenate((G[:K, _2K:_3K], G[K:_2K, :K]), axis=1)
ans = G.max()
print(ans)
