

def main():
    N, M = [int(x) for x in input().split()]
    arrs = []
    for _ in range(M):
        arrs.append([int(x) - 1 for x in input().split()])
    print(solve(N, M, arrs))


def solve(N, M, arrs):
    next_arr = [None] * N
    arr = arrs[0]
    for r, nr in zip(arr, arr[1:]):
        next_arr[r] = nr
    for i in range(1, M):
        read = arrs[i]
        next_arr_new = [None] * N
        for r, nr in zip(read, read[1:]):
            next_arr_new[r] = nr
        for r, nr in enumerate(next_arr_new):
            if next_arr[r] != nr:
                next_arr[r] = None

    starts = []
    cycs = []
    curr = 0
    for r in arr:
        if next_arr[r] != None:
            if curr == 0:
                starts.append(r)
            curr += 1
        elif curr > 0:
            cycs.append(curr)
            curr = 0
    if curr > 0:
        cycs.append(curr)

    assert len(starts) == len(cycs)

    s = 0
    for c in cycs:
        s += c * (c + 1) // 2
    s += N

    return s


solve(3, 2, [[0, 1, 2], [0, 1, 2]])


def solve_naive(r1, r2):
    count = 0
    for i in range(len(r1)):
        for j in range(i + 1, len(r1) + 1):
            for ii in range(len(r2)):
                l = j - i
                if r1[i:j] == r2[ii:ii + l]:
                    count += 1
    return count


def test(N):
    from random import shuffle
    for i in range(1000):
        r1 = list(range(N))
        r2 = list(range(N))
        shuffle(r1)
        shuffle(r2)
        res = solve(N, 2, [r1, r2])
        res2 = solve_naive(r1, r2)
        if res != res2:
            print(r1, r2)
            print(res, res2)
            assert res == res2


main()
