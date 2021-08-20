import sys
input = sys.stdin.readline


def main():
    (N, K) = map(int, input().split())
    (R, S, P) = map(int, input().split())
    T = list(input().rstrip())
    D = [[] for _ in range(K)]
    for (i, t) in enumerate(T):
        D[i % K].append(t)
    ans = 0
    for List in D:
        pre = -1
        for (i, p) in enumerate(List):
            if p == 'r':
                s = P
            elif p == 's':
                s = R
            else:
                s = S
            if pre != p:
                ans += s
                pre = p
            else:
                pre = -1
    print(ans)


def __starting_point():
    main()


__starting_point()
