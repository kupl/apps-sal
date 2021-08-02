def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    import bisect
    import collections
    colormax = collections.deque([A[0]])
    for i in range(1, N):
        idx = bisect.bisect_left(colormax, A[i])
        if idx == 0:
            colormax.appendleft(A[i])
        else:
            colormax[idx - 1] = A[i]
    print(len(colormax))


if '__main__' == __name__:
    resolve()
