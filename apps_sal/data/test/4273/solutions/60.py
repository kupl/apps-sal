import sys
import itertools

input = sys.stdin.readline


def main():
    N = int(input())
    l = ['M', 'A', 'R', 'C', 'H']
    m = [0] * 5
    for _ in range(N):
        S = input()[:-1]
        Shead = S[0]
        for i, s0 in enumerate(l):
            if Shead == s0:
                m[i] += 1
                break
    ll = []
    for i, n in enumerate(m):
        if n >= 1:
            ll.append(l[i])
    if len(ll) <= 2:
        print((0))
        return
    ans = 0
    for i, j, k in itertools.combinations(ll, 3):
        ans += m[l.index(i)] * m[l.index(j)] * m[l.index(k)]

    print(ans)


def __starting_point():
    main()


__starting_point()
