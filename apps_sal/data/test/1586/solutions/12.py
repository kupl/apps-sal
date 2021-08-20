import sys
input = sys.stdin.readline


def main():
    N = int(input())
    if N % 2 == 1:
        print(0)
        return
    count = []
    i = 0
    while True:
        q = N // (10 * 5 ** i)
        if q == 0:
            break
        else:
            count.append((q, i + 1))
            i += 1
    ans = 0
    prev_c = 0
    for (c, n_zero) in count[::-1]:
        ans += n_zero * (c - prev_c)
        prev_c = c
    print(ans)


def __starting_point():
    main()


__starting_point()
