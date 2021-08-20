import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main():
    n = int(input())
    aa = list(map(int, input().split()))
    s = 0
    for a in aa:
        s ^= a
    for i in range(n):
        aa[i] &= ~s
    rnk = 0
    for k in range(60, -1, -1):
        mask = 1 << k
        for i in range(rnk, n):
            if mask & aa[i]:
                (aa[i], aa[rnk]) = (aa[rnk], aa[i])
                break
        else:
            continue
        for i in range(n):
            if i == rnk:
                continue
            if aa[i] & mask:
                aa[i] ^= aa[rnk]
        rnk += 1
    red = 0
    for i in range(rnk):
        red ^= aa[i]
    blue = s ^ red
    print(s + 2 * (red & blue))


main()
