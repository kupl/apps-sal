#!/usr/bin/env python3
import math


def main():
    N = int(input())
    T, A = list(map(int, input().split()))
    for _ in range(N - 1):
        t, a = list(map(int, input().split()))
        # 桁が大きいとfloatの誤差が生じて正しく判定できない
        # 負の数にして切り捨てにすればceilと同じ挙動になる
        x = max(-(-T // t), -(-A // a))
        T = t * x
        A = a * x
    print((T + A))


def __starting_point():
    main()


__starting_point()
