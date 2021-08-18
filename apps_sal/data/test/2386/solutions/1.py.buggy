N = int(input())
A = [int(i) for i in input().split()]
A = [A[i] - i - 1 for i in range(N)]
A.sort()


def snk(b):
    res = 0
    for i in range(N):
        res += abs(A[i] - b)
    return res


if N == 1:
    print(snk(A[N // 2]))
    return
print(min(snk(A[N // 2]), snk(A[N // 2 + 1])))
