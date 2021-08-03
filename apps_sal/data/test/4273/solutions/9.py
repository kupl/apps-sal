import sys
input = sys.stdin.readline


def main():
    N = int(input())
    L = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for i in range(N):
        S = input().rstrip()
        if S[0] in L:
            L[S[0]] += 1
    CNT = 0
    i = 0
    S = [0] * 5
    for k, v in L.items():
        S[i] = v
        i += 1
    ans = 0
    for p in range(3):
        for q in range(p + 1, 4):
            for r in range(q + 1, 5):
                ans += S[p] * S[q] * S[r]
    print(ans)


def __starting_point():
    main()


__starting_point()
