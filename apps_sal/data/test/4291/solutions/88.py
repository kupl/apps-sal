from bisect import bisect_left, bisect_right


def main():
    N, Q = list(map(int, input().split()))
    S = input()
    s = []
    for i in range(N - 1):
        if S[i] + S[i + 1] == 'AC':
            s.append(i)

    for q in range(Q):
        l, r = list(map(int, input().split()))
        ans = bisect_left(s, r - 1) - bisect_left(s, l - 1)
        print(ans)


def __starting_point():
    main()


__starting_point()
