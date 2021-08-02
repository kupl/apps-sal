def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    N, P = map(int, input().split())
    S = input().rstrip()
    if P in (2, 5):
        ans = 0
        for i, c in enumerate(S):
            if int(c) % P == 0:
                ans += i + 1
        print(ans)
        return
    num = 0
    d = 1
    counter = defaultdict(int)
    counter[0] += 1
    for c in S[::-1]:
        num += int(c) * d
        num %= P
        counter[num] += 1
        d *= 10
        d %= P
    ans = 0
    for v in counter.values():
        ans += (v * (v - 1)) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
