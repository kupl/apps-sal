import bisect as bs


def main():
    with open(0) as f:
        N = int(f.readline())
        A = sorted(list(map(int, f.readline().split())))
        B = list(map(int, f.readline().split()))
        C = sorted(list(map(int, f.readline().split())))

    ans = 0
    for b in B:
        ans += bs.bisect_left(A, b) * (N - bs.bisect_right(C, b))
    print(ans)


main()
