#!/usr/bin/env python3
from collections import deque
from bisect import bisect_left


def main():
    N, *A = map(int, open(0))
    # 方針: 色ごとに最大値をリストで保持する
    # 新しく色を追加しないといけない時は持っている全ての数字より小さい時->先頭追加なのでdequeがいい
    # dequeをbisectで二分探索できるんだ...
    q = deque([])
    for i in range(N):
        d = bisect_left(q, A[i])
        if d == 0:
            q.appendleft(A[i])
        else:
            q[d - 1] = A[i]
    print(len(q))


def __starting_point():
    main()


__starting_point()
