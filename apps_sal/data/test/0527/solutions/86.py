import bisect


def main() -> None:
    S = input()
    T = input()
    SS = S + S
    alphas = [[] for _ in range(26)]
    for i, s in enumerate(SS):
        alphas[ord(s) - ord('a')].append(i)
    rep, now = 0, -1
    for t in T:
        alpha = alphas[ord(t) - ord('a')]
        i = bisect.bisect_left(alpha, now + 1)
        if i == len(alpha):
            print((-1))
            return
        now = alpha[i]
        if now >= len(S):
            now -= len(S)
            rep += 1
    print((rep * len(S) + now + 1))



def __starting_point():
    main()

__starting_point()
