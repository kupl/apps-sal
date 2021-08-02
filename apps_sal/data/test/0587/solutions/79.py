
# -*-coding: utf-8 -*-

import sys


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    S = [tuple(map(int, input().split())) for _ in range(n)]
    S.sort(key=lambda x: -x[1])
    y_1, y_0 = [0], [0]
    st = set()

    for t, d in S:
        if t in st:
            # 累積報酬和のリスト
            y_0.append(y_0[-1] + d)
        else:
            st.add(t)
            y_1.append(y_1[-1] + d)

    max_sum = -1

    for i in range(1, k + 1):
        if k - i >= len(y_0):
            continue
        if i >= len(y_1):
            break
        max_sum = max(max_sum, y_0[k - i] + y_1[i] + i**2)

    print(max_sum)
    return


def __starting_point():
    main()


__starting_point()
