#!/usr/bin/env python3

def main():
    n, m = list(map(int, input().split()))
    A = [input() for i in range(n)]
    B = [input() for i in range(m)]
    for i in range(n):
        C = []
        p = A[i].find(B[0])
        if p != -1:
            for j in range(m):
                if i + j < n and p + len(B[0]) <= n:
                    C.append(A[i + j][p:p + len(B[0])])
            if C == B:
                break

    print(('Yes' if C == B else 'No'))


def __starting_point():
    main()


__starting_point()
