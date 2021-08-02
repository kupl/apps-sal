import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()
def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W, K = NMI()
    choco = [SI() for _ in range(H)]
    ans = 100000
    for case in range(2**(H - 1)):
        groups = [[0]]
        for i in range(H - 1):
            if (case >> i) & 1:
                groups[-1].append(i + 1)
            else:
                groups.append([i + 1])
        white = [0] * len(groups)

        is_badcase = False
        cut = len(groups) - 1
        for w in range(W):
            diff = [0] * len(groups)
            for gi, group in enumerate(groups):
                for h in group:
                    if choco[h][w] == "1":
                        white[gi] += 1
                        diff[gi] += 1

            if max(white) <= K:
                is_cont = True
                continue

            if max(diff) > K:
                is_badcase = True
                break

            cut += 1
            white = diff[:]
            continue

        if not is_badcase:
            ans = min(ans, cut)

    print(ans)


def __starting_point():
    main()


__starting_point()
