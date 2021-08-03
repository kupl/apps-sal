def solve(seq):
    n = len(seq)
    cnt = [0] * 5001
    for e in seq:
        cnt[e] += 1

    acc = [0]
    for i in range(1, 5001):
        acc.append(acc[-1] + cnt[i])

    ans = n
    for i in range(5001):
        if cnt[i] > 0:
            n2remove = n - acc[min(2 * i, 5000)] + acc[i - 1]
            ans = min(ans, n2remove)

    return ans


def main():
    with open('input.txt') as f:
        _ = int(f.readline())
        seq = list(map(int, f.readline().split()))

    ans = solve(seq)

    with open('output.txt', 'w') as f:
        f.write(str(ans))


def __starting_point():
    main()


__starting_point()
