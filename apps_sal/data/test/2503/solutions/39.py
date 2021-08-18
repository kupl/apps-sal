def d_checker():
    import numpy as np
    N, K = [int(i) for i in input().split()]

    def get_bound(p):
        """ある希望を満たすような角のマスの集合はKxK正方形区間のようになっている
        p<K-1 のときはその正方形を分割しないとならない"""
        return [(0, p + 1), (p + K + 1, 2 * K)] if p < K - 1 else [(p - K + 1, p + 1)]

    requests_black = [[0] * (2 * K + 1) for _ in range(2 * K + 1)]
    for _ in range(N):
        x, y, c = input().split()
        x = int(x) % (2 * K)
        y = int(y) % (2 * K) if c == 'B' else (int(y) + K) % (2 * K)

        for shift in (0, K):
            for b, t in get_bound((y + shift) % (2 * K)):
                for l, r in get_bound((x + shift) % (2 * K)):
                    requests_black[b][l] += 1
                    requests_black[t][l] -= 1
                    requests_black[b][r] -= 1
                    requests_black[t][r] += 1
    return int(np.max(np.cumsum(np.cumsum(requests_black, axis=1), axis=0)))


print(d_checker())
