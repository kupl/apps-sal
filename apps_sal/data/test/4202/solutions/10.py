import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def main():
    l, r = list(map(int, input().split()))
    diff = r - l
    if diff >= 2018:
        return 0

    else:
        min_ = 2 ** 20
        # l の商と余り
        p = l // 2019
        q = l % 2019
        for xi in range(l, r):
            qi = (q + (xi - l)) % 2019
            if qi == 0:
                return 0
            for xj in range(xi + 1, r + 1):
                qj = (q + (xj - l)) % 2019
                if qj == 0:
                    return 0
                else:
                    qij = (qi * qj) % 2019
                    if qij < min_:
                        min_ = qij

    return min_


print(main())
