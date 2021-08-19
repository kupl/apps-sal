import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    noInOuts = [None] * (2 * N + 1)
    fIns = [-1] * (N + 1)
    fOuts = [-1] * (N + 1)
    for no in range(1, N + 1):
        (A, B) = list(map(int, input().split()))
        if A != -1:
            if noInOuts[A] is not None:
                return False
            noInOuts[A] = (no, 'in')
            fIns[no] = A
        if B != -1:
            if noInOuts[B] is not None:
                return False
            noInOuts[B] = (no, 'out')
            fOuts[no] = B

    def check(fr, to):
        L = (to + 1 - fr) // 2
        for i in range(L):
            if noInOuts[fr + i] is not None:
                (no, dire) = noInOuts[fr + i]
                if dire == 'in':
                    if noInOuts[fr + i + L] is not None:
                        (no2, dire2) = noInOuts[fr + i + L]
                        if no2 != no:
                            return False
                    elif fOuts[no] != -1:
                        return False
                else:
                    return False
        for i in range(L):
            if noInOuts[fr + i + L] is not None:
                (no, dire) = noInOuts[fr + i + L]
                if dire == 'out':
                    if noInOuts[fr + i] is not None:
                        (no2, dire2) = noInOuts[fr + i]
                        if no2 != no:
                            return False
                    elif fIns[no] != -1:
                        return False
                else:
                    return False
        return True
    dp = [False] * (2 * N + 1)
    dp[0] = True
    for i in range(0, 2 * N, 2):
        if not dp[i]:
            continue
        for j in range(i + 2, 2 * N + 1, 2):
            if check(i + 1, j):
                dp[j] = True
    return dp[2 * N]


if solve():
    print('Yes')
else:
    print('No')
