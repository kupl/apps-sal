from collections import Counter
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    S = input()
    ans = 0
    (r, g, b) = ([0 for _ in range(N + 1)], [0 for _ in range(N + 1)], [0 for _ in range(N + 1)])
    for i in range(N):
        (r[i + 1], g[i + 1], b[i + 1]) = (r[i], g[i], b[i])
        if S[i] == 'R':
            r[i + 1] += 1
        elif S[i] == 'G':
            g[i + 1] += 1
        else:
            b[i + 1] += 1
    for i in range(1, N - 1):
        if S[i] == 'R':
            ans += g[i] * (b[N] - b[i + 1]) + b[i] * (g[N] - g[i + 1])
            for j in range(1, min(i, N - i - 1) + 1):
                if {S[i - j], S[i + j]} == {'G', 'B'}:
                    ans -= 1
        elif S[i] == 'G':
            ans += r[i] * (b[N] - b[i + 1]) + b[i] * (r[N] - r[i + 1])
            for j in range(1, min(i, N - i - 1) + 1):
                if {S[i - j], S[i + j]} == {'R', 'B'}:
                    ans -= 1
        elif S[i] == 'B':
            ans += g[i] * (r[N] - r[i + 1]) + r[i] * (g[N] - g[i + 1])
            for j in range(1, min(i, N - i - 1) + 1):
                if {S[i - j], S[i + j]} == {'G', 'R'}:
                    ans -= 1
    print(ans)


main()
