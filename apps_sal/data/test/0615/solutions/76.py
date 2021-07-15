#!/usr/bin/env python3
import sys
import itertools
INF = float("inf")


def solve(N: int, A: "List[int]"):

    wa = list(itertools.accumulate(A))
    # print(wa)
    m = INF
    # しゃくとり法
    atama1, atama2 = 0, 2
    # 真ん中iを固定する
    for i in range(1, N-2):
        # 0からi-1までの分割位置を決める
        # 最も前後の数列の和が近くなるように

        # 前の虫
        s0, s1 = wa[atama1], wa[i]-wa[atama1]
        for j in range(atama1+1, i):
            t0, t1 = wa[j], wa[i]-wa[j]
            # print(s0, s1, t0, t1, atama1)
            if t0 >= t1:
                if abs(s1-s0) >= abs(t1-t0):
                    s0, s1 = t0, t1
                    atama1 += 1
                break
            s0, s1 = t0, t1
            atama1 += 1
        # print(s0, s1, t0, t1)

        # 後ろの虫
        s2, s3 = wa[atama2]-wa[i], wa[N-1]-wa[atama2]
        for j in range(atama2+1, N):
            t2, t3 = wa[j]-wa[i], wa[N-1]-wa[j]
            if t2 >= t3:
                if abs(s3-s2) >= abs(t3-t2):
                    s2, s3 = t2, t3
                    atama2 += 1
                break
            s2, s3 = t2, t3
            atama2 += 1

        s = [s0, s1, s2, s3]
        # print(s)
        s.sort()
        m = min(s[3]-s[0], m)

    print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


def __starting_point():
    main()

__starting_point()
