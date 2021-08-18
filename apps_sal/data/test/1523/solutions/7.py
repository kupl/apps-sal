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


def main():
    n, k = srl(int)
    A = srl(int)
    B = srl(int)
    spare = []
    done = [-1] * k
    for i in range(n):
        task = A[i] - 1
        if done[task] == -1:
            done[task] = B[i]
            continue
        spare.append(min(done[task], B[i]))
        done[task] = max(done[task], B[i])
    spare.sort()
    i = 0
    r = 0
    for d in done:
        if d == -1:
            r += spare[i]
            i += 1
    print(r)


def __starting_point():
    main()


__starting_point()
