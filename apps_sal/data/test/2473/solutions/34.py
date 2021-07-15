import sys
import numpy as np
input = sys.stdin.readline

def main():
    N, K = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for i in range(N)]
    # 座標圧縮
    xs = []
    ys = []
    xy = sorted(xy, key=lambda x: x[0])
    for i in range(N):
        xs.append(xy[i][0])
        xy[i][0] = i+1
    xy = sorted(xy, key=lambda x: x[1])
    for i in range(N):
        ys.append(xy[i][1])
        xy[i][1] = i+1
    # 2次元累積和
    sum_ = np.zeros((N+1, N+1), dtype=int)
    for i in range(N):
        x, y = xy[i]
        sum_[y][x] = 1
    for i in range(1, N+1):
        sum_[i] += sum_[i-1]
    for i in range(1, N+1):
        sum_[:,i] += sum_[:,i-1]
    # 全探索
    ans = int(1e20)
    for l in range(1, N+1):
        no_three = True
        for r in range(N, l, -1):
            no_two = True
            for d in range(1, N+1):
                no_one = True
                for u in range(d+1, N+1):
                    tmp = sum_[u][r] - sum_[d-1][r] - sum_[u][l-1] + sum_[d-1][l-1]
                    if tmp >= K:
                        tmp = (xs[r-1] - xs[l-1]) * (ys[u-1] - ys[d-1])
                        ans = min(ans, tmp)
                        no_one = False
                        break
                if no_one:
                    break
                else:
                    no_two = False
            if no_two:
                break
            else:
                no_three = False
        if no_three:
            break
                

    print(ans)

def __starting_point():
    main()

__starting_point()
