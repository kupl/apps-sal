import numpy as np

def main():
    H, W, K = list(map(int, input().split()))
    S = []
    for _ in range(H):
        S.append(list(map(int, list(input()))))
    S = np.array(S)
    if S.sum() <= K:
        print((0))
        return
    answer = float('INF')
    for i in range(0, 2 ** (H - 1)):
        horizons = list(map(int, list(bin(i)[2:].zfill(H - 1))))
        result = greedy(W, S, K, horizons, answer)
        answer = min(answer, result)
    print(answer)

# ex. horizons = [0, 0, 1, 0, 0, 1]
def greedy(W, S, K, horizons, current_answer):
    answer = sum(horizons)
    # ex.
    # S  = [[1, 1, 1, 0, 0],
    #       [1, 0, 0, 0, 1],
    #       [0, 0, 1, 1, 1]]
    # horizons = [0, 1]のとき,
    # S2 = [[2, 1, 1, 0, 0],
    #       [0, 0, 1, 1, 1]]
    # となる
    top = 0
    bottom = 0
    S2 = []
    for h in horizons:
        if h == 1:
            S2.append(S[:][top:(bottom + 1)].sum(axis=0).tolist())
            top = bottom + 1
        bottom += 1
    S2.append(S[:][top:].sum(axis=0).tolist())
    # ブロック毎の累積和を計算する
    h = len(S2)
    partial_sums = [0] * h
    for right in range(W):
        current = [0] * h
        for idx in range(h):
            current[idx] = S2[idx][right]
            partial_sums[idx] += S2[idx][right]
        # 1列に含むホワイトチョコの数がkより多い場合
        if max(current) > K:
            return float('INF')
        # 無理な(ブロックの中のホワイトチョコの数をk以下にできない)場合
        if max(partial_sums) > K:
            answer += 1
            if answer >= current_answer:
                return float('INF')
            partial_sums = current
    return answer

def __starting_point():
    main()

__starting_point()
