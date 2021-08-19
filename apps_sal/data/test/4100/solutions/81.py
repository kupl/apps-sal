# coding: utf-8

def main():
    N, K, Q = list(map(int, input().split()))
    A = [0] * N

    for _ in range(Q):
        tmp = int(input())
        A[tmp - 1] += 1

    for i in range(N):
        if A[i] + K > Q:
            print('Yes')
        else:
            print('No')


def __starting_point():
    main()


__starting_point()
