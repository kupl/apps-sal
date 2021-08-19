import sys
input = sys.stdin.readline


def main():
    n = int(input())
    A = list(map(int, input().split()))
    F = [int()] * n
    F[0] = A[0]
    for b in range(1, n):
        F[b] = F[b - 1] + A[b]
    res = [0] * 4
    data = [10 ** 18] * 2
    ex = [0] * 4
    ans = 10 ** 18
    s = 0
    t = 2
    for i in range(1, n - 2):
        bl = [True, True]
        for j in range(s, i):
            res[0] = F[j]
            res[1] = F[i] - F[j]
            if not bl[0]:
                break
            if data[0] > abs(res[1] - res[0]) or j == s:
                s = j
                ex[0] = res[0]
                ex[1] = res[1]
                data[0] = abs(res[1] - res[0])
            else:
                bl[0] = False
        for k in range(t, n):
            res[2] = F[k] - F[i]
            res[3] = F[n - 1] - F[k]
            if not bl[1]:
                break
            if data[1] > abs(res[3] - res[2]) or k == t:
                t = k
                ex[2] = res[2]
                ex[3] = res[3]
                data[1] = abs(res[3] - res[2])
            else:
                bl[1] = False
        ans = min(ans, max(ex) - min(ex))
    print(ans)


def __starting_point():
    main()


__starting_point()
