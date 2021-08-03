from collections import defaultdict as di
import sys
input = iter(sys.stdin.read().splitlines()).__next__


def solve():
    n, m = map(int, input().split())
    B = [input() for _ in range(n)]

    pos = di(list)
    for i in range(n):
        b = B[i]
        for j in range(m):
            pos[b[j]].append((i, j))
    if '.' in pos:
        del pos['.']

    C = [list('.' * m) for _ in range(n)]
    moves = []

    if pos:
        mxx = max(pos)
        for i in range(97, ord(mxx) + 1):
            c = chr(i)
            if c not in pos:
                pos[c] = pos[mxx]
            P = pos[c]
            if all(p[0] == P[0][0] for p in P):
                mn = min(p[1] for p in P)
                mx = max(p[1] for p in P)
                i = P[0][0]
                for j in range(mn, mx + 1):
                    C[i][j] = c
                moves.append((i + 1, mn + 1, i + 1, mx + 1))
            elif all(p[1] == P[0][1] for p in P):
                mn = min(p[0] for p in P)
                mx = max(p[0] for p in P)
                j = P[0][1]
                for i in range(mn, mx + 1):
                    C[i][j] = c
                moves.append((mn + 1, j + 1, mx + 1, j + 1))

    if [''.join(s) for s in C] == B:
        print('YES')
        print(len(moves))
        for m in moves:
            print(*m)
    else:
        print('NO')


def main():
    t = int(input())

    for _ in range(t):
        solve()


main()
