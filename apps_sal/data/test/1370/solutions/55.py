# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, K, Si):
    Si = [[int(i) for i in S] for S in Si]
    ans = H + W
    for i in range(2 ** (H - 1)):
        h_border = bin(i).count('1')
        w_border = 0
        white_counts = [0] * (h_border + 1)
        choco_w = 0
        for w in range(W):
            choco_w += 1
            wc_num = 0
            tmp_count = [0] * (h_border + 1)
            for h in range(H):
                white_counts[wc_num] += Si[h][w]
                tmp_count[wc_num] += Si[h][w]
                if i >> h & 1:
                    wc_num += 1
            if max(white_counts) > K:
                if choco_w == 1:
                    break  # 1列の時点で > K の場合は条件を達成できない
                w_border += 1
                white_counts = tmp_count
                choco_w = 1
        else:
            ans = min(ans, h_border + w_border)
    print(ans)


def __starting_point():
    H, W, K = list(map(int, input().split()))
    Si = [input() for _ in range(H)]
    solve(H, W, K, Si)

    # # test
    # from random import randint
    # from func import random_str
    # 
    # H, W, K = 10, 1000, randint(1, 100)
    # Si = [random_str(W, '01') for _ in range(H)]
    # print(H, W, K)
    # for S in Si:
    #     print(S)
    # solve(H, W, K, Si)

__starting_point()
