import sys
import math
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(100000)
MOD = 1000000007


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def solve():
    seqs = []
    tmp = "X"
    seq = 0
    st = input().strip()
    n = len(st)
    for ch in st:
        if ch == "m" or ch == "w":
            print(0)
            return
        elif ch in ["u", "n"]:
            if tmp == ch:
                seq += 1
            else:
                if seq != 0:
                    seqs.append(seq)
                seq = 1

        else:
            if seq != 0:
                seqs.append(seq)
            seq = 0

        tmp = ch
    if seq != 0:
        seqs.append(seq)

    nst = [0 for i in range(n + 2)]
    mst = [0 for i in range(n + 2)]
    nst[1] = 1
    for i in range(2, n + 1):
        nst[i] = (nst[i - 1] + mst[i - 1]) % MOD
        mst[i] = nst[i - 1] % MOD

    ans = 1
    for seq in seqs:
        ans *= nst[(seq)] + mst[(seq)]
        ans %= MOD
    print(ans)

    return


def main():
    solve()


def __starting_point():
    main()


__starting_point()
