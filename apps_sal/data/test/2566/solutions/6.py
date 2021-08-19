import sys
3


def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()


def srl(proc=None):
    if proc is not None:
        return list(map(proc, rl().split()))
    else:
        return rl().split()


def test(K, A, i):
    r = 0
    while K > 0:
        if A[(r + i) % 7]:
            K -= 1
        r += 1
    return r


def brute(K, A):
    best = 1 << 60
    for i in range(7):
        if A[i]:
            best = min(best, test(K, A, i))
    return best


def solve(K, A):
    s = sum(A)
    if s == 0:
        return -1
    if K < 32:
        return brute(K, A)
    full_weeks = (K - 2 * s) // s
    K -= full_weeks * s
    return 7 * full_weeks + brute(K, A)


def main():
    T = rl(int)
    for t in range(1, T + 1):
        K = rl(int)
        A = srl(int)
        print(solve(K, A))


def __starting_point():
    main()


__starting_point()
