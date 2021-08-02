
def solve(n, x, seq):
    x -= 1
    _min = min(seq)
    s = sum(seq)
    idx = -1
    for i in range(x, -1, -1):
        if seq[i] == _min:
            idx = i
            break
    else:
        for j in range(n - 1, x, -1):
            if seq[j] == _min:
                idx = j
                break

    for i in range(n):
        seq[i] -= _min

    if idx <= x:
        for j in range(idx + 1, x + 1):
            seq[j] -= 1
    else:
        for j in range(x, -1, -1):
            seq[j] -= 1

        for j in range(n - 1, idx, -1):
            seq[j] -= 1

    seq[idx] = s - sum(seq)
    return seq


def main():
    n, x = list(map(int, input().split()))
    seq = [int(c) for c in input().split()]
    ans = solve(n, x, seq)
    print(*ans)


def __starting_point():
    main()


__starting_point()
