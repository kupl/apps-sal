#!/usr/bin/env python3

import sys
import heapq
import bisect
sys.setrecursionlimit(300000)


def _count(A, n, v):
    ret = 0
    for a in A:
        target = v - a
        idx = bisect.bisect_left(A, target)
        ret += n - idx
    return ret


def _sum(A, n, v, sums):
    ss = 0
    for a in A:
        target = v - a
        idx = bisect.bisect_left(A, target)
        ss += sums[n] - sums[idx]
        ss += (n - idx) * a
    # print(mins)
    return ss


def solve(N: int, M: int, A: "List[int]"):
    A.sort()
    sums = [0]
    for a in A:
        sums.append(sums[-1] + a)
    l = -1
    r = max(A) * 2 + 1
    while r - l > 1:
        m = (r + l) // 2
        cnt = _count(A, N, m)
        if cnt >= M:
            l = m
        else:
            r = m
    cnt = _count(A, N, l)
    ret = _sum(A, N, l, sums)
    ret -= (cnt - M) * l
    print(ret)
    return ret


def solve_(N: int, M: int, A: "List[int]"):
    A.sort(reverse=True)
    q = [(-A[0] * 2, 0, 0)]
    ret = 0
    cnt = 0
    while cnt < M:
        s, i, j = heapq.heappop(q)
        ret += -s
        cnt += 1
        print((i, j))
        if i == j and i < N - 1:
            heapq.heappush(q, (-A[i] + -A[i + 1], i, i + 1))
        else:
            if cnt < M:
                ret += -s
                cnt += 1
                print((j, i))
            heapq.heappush(q, (-A[i + 1] + -A[j], i + 1, j))
            if j < N - 1:
                heapq.heappush(q, (-A[i] + -A[j + 1], i, j + 1))
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


def __starting_point():
    main()


__starting_point()
