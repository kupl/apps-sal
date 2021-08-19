def main():
    import sys
    input = sys.stdin.readline
    (n, m) = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(m)]
    BC = sorted(BC, key=lambda x: x[1], reverse=True)
    append_list = []
    for (b, c) in BC:
        if len(append_list) >= n:
            break
        append_list += [c] * b
    A += append_list
    A.sort(reverse=True)
    print(sum(A[:n]))


def __starting_point():
    main()


__starting_point()
