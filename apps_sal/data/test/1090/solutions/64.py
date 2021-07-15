# https://drken1215.hatenablog.com/entry/2020/05/16/005300

def main():
    from itertools import tee

    N, K = list(map(int, input().split()))
    S = input()

    s1, s2 = tee(S, 2)
    next(s2)

    cnt = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            cnt += 1

    ans = N - 1 - max(cnt - K * 2, 0)

    print(ans)


def __starting_point():
    main()

__starting_point()
