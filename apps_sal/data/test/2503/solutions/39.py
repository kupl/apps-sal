def d_checker():
    # 参考1: https://pitsbuffersolution.com/compro/atcoder/arc089d.php
    # 参考2: https://atcoder.jp/contests/abc086/submissions/3271380
    import numpy as np
    N, K = [int(i) for i in input().split()]

    def get_bound(p):
        """ある希望を満たすような角のマスの集合はKxK正方形区間のようになっている
        p<K-1 のときはその正方形を分割しないとならない"""
        return [(0, p + 1), (p + K + 1, 2 * K)] if p < K - 1 else [(p - K + 1, p + 1)]

    # マス(x, y)が白⇔マス(x, y+K)が黒なので、希望の色を黒に統一する
    # 市松模様の周期は2Kなので、x, y座標をそれぞれ2Kで剰余を取った座標と同一視できる
    requests_black = [[0] * (2 * K + 1) for _ in range(2 * K + 1)]
    for _ in range(N):
        x, y, c = input().split()
        x = int(x) % (2 * K)
        y = int(y) % (2 * K) if c == 'B' else (int(y) + K) % (2 * K)

        for shift in (0, K):  # 2Kx2Kの市松模様の中に同色の領域が2つずつあることを反映
            # bottom, top, left, right
            for b, t in get_bound((y + shift) % (2 * K)):
                for l, r in get_bound((x + shift) % (2 * K)):
                    # 2次元imos法(左上、左下、右上、右下に±1することと対応)
                    requests_black[b][l] += 1
                    requests_black[t][l] -= 1
                    requests_black[b][r] -= 1
                    requests_black[t][r] += 1
    # 最後に累積和を取ると、あるマスを正方形の角としたとき叶えられる希望の数がわかる
    return int(np.max(np.cumsum(np.cumsum(requests_black, axis=1), axis=0)))

print(d_checker())
