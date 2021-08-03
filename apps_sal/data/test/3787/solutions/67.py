def main():
    N, A, B = list(map(int, input().split()))
    if N < A:
        print((-1))
        return
    x = -(-N // A)
    if B < x or (N - A + 1) < B:
        print((-1))
        return
    lst = list(range(1, N + 1))
    seq = [lst[:A]]
    idx = A
    for i in range(B - 1):
        rem = B - 1 - i
        nidx = idx - (-(N - idx) // rem)
        seq.append(lst[idx:nidx])
        idx = nidx
    ans = []
    for s in reversed(seq):
        ans += s
    print((*ans))


def __starting_point():
    main()


__starting_point()
