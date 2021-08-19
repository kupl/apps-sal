from collections import defaultdict


def read():
    N = int(input().strip())
    S = input().strip()
    return (N, S)


def solve(N, S):
    low = 0
    high = (N >> 1) + 1
    while high - low > 1:
        mid = high + low >> 1
        is_match = False
        m = N - mid + 1
        d = defaultdict(list)
        for i in range(0, m):
            d[S[i:i + mid]].append(i)
        for v in d.values():
            if v[-1] - v[0] >= mid:
                is_match = True
                break
        if is_match:
            low = mid
        else:
            high = mid
    return low


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print('%s' % str(outputs))


__starting_point()
