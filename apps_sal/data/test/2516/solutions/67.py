from collections import defaultdict


def main():
    N, P = list(map(int, input().split()))
    S = input()
    if P in [2, 5]:
        ans = 0
        for right in range(N - 1, - 1, - 1):
            if int(S[right]) % P == 0:
                ans += right + 1
        print(ans)
        return
    cur_c = 0
    C = [0] * N
    pw = 1
    for n, s in enumerate(S[::-1]):
        cur_c = (cur_c + pw * int(s)) % P
        C[N - 1 - n] = cur_c
        pw = (pw * 10) % P
    counter = defaultdict(int)
    for c in C:
        counter[c] += 1
    ans = 0
    for c in C:
        counter[c] -= 1
        ans += counter[c]
    ans += len([c for c in C if c == 0])
    print(ans)


def __starting_point():
    main()


__starting_point()
