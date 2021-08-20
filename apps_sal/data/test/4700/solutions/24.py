import sys
pin = sys.stdin.readline


def main():
    (N, M) = map(int, pin().split())
    H = list(map(int, pin().split()))
    d = [True] * N
    ans = 0
    for _ in [0] * M:
        (A, B) = map(int, pin().split())
        if H[A - 1] > H[B - 1]:
            d[B - 1] = False
        elif H[B - 1] > H[A - 1]:
            d[A - 1] = False
        else:
            d[A - 1] = False
            d[B - 1] = False
    for i in d:
        if i:
            ans += 1
    print(ans)
    return


main()
