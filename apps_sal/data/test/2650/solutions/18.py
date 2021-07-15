# codekata from https://atcoder.jp/contests/abc170/submissions/14456317
# by puzzlesolver

import sys
import heapq


input = sys.stdin.readline

def main():

    N, Q = [int(x) for x in input().split()]

    hsize = 2 * 10 ** 5 + 1

    h = [[] for _ in range(hsize)]

    # 園児が現在所属している幼稚園を保存
    C = [0] * N
    A = []

    for i in range(N):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        heapq.heappush(h[b], (-a, i))
        C[i] = b

    A = tuple(A)

    byodo = []

    for i in range(1, hsize):
        if len(h[i]) == 0:
            continue

        # 各幼稚園の最大値をbyodoに入れる

        x = h[i][0]
        heapq.heappush(byodo, (-x[0], x[1]))

    ans = []
    for _ in range(Q):
        c, d = [int(x) for x in input().split()]
        c -= 1

        # 移動元最大値チェック
        cfrom = C[c]
        # c園児の現在時をdに更新
        C[c] = d

        while h[cfrom]:
            x = h[cfrom][0]
            # 最大値の園児の現在の所属幼稚園がC[c]と異なればpopしたままにする
            if C[x[1]] != cfrom:
                heapq.heappop(h[cfrom])
                continue

            # 現在の最大値を平等にpush
            heapq.heappush(byodo, (-x[0], x[1]))
            break

        # c園児をd幼稚園にpush
        heapq.heappush(h[d], (-A[c], c))

        # 移動先最大値チェック
        while h[d]:
            x = h[d][0]
            # 最大値の園児の現在の所属幼稚園がdと異なればpopしたままにする
            if C[x[1]] != d:
                heapq.heappop(h[d])
                continue

            # 現在の最大値をbyodoにpush
            heapq.heappush(byodo, (-x[0], x[1]))
            break

        # 平等の最小値を取得

        while byodo:
            x = byodo[0]


            # 最小値が所属する幼稚園の最大値が異なっていればpopしたままにする
            y = h[C[x[1]]][0]
            if -y[0] != x[0]:
                heapq.heappop(byodo)
                continue

            ans.append(x[0])
            break

    print(('\n'.join(map(str, ans))))


def __starting_point():
    main()

__starting_point()
