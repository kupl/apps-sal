import sys


def like2017(N):

    D = [True] * (N + 1)
    L = [0] * (N + 1)

    D[0] = False
    D[1] = False

    for n in range(2, N + 1):
        if not D[n]:
            continue

        for k in range(2, N // n + 1):
            D[k * n] = False

    cnt = 0
    for n in range(1, N + 1):
        if D[n] and D[(n + 1) // 2] and n % 2 == 1:
            cnt += 1
        L[n] = cnt

    return L


def main():
    Q = int(sys.stdin.readline().rstrip())

    L = like2017(10**5)

    for _ in range(Q):
        l, r = list(map(int, sys.stdin.readline().rstrip().split()))
        print((L[r] - L[l - 1]))


main()
