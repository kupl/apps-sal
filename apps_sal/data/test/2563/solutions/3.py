import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    A = [int(a) for a in input()]
    N = len(A)
    O = []
    E = []
    for i in range(N):
        if A[i] % 2:
            O.append(A[i])
        else:
            E.append(A[i])
    O = O[::-1]
    E = E[::-1]
    B = []
    while O or E:
        if not O:
            B.append(E.pop())
        elif not E:
            B.append(O.pop())
        elif O[-1] < E[-1]:
            B.append(O.pop())
        else:
            B.append(E.pop())
    print(''.join(map(str, B)))
