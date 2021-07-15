import sys

input = sys.stdin.readline


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    K_d = [0] * (len(bin(10 ** 12)) - 2)
    L = len(K_d)
    for i, k in enumerate(bin(K)[2:][::-1], 1):
        k = int(k)
        K_d[L - i] = k

    cnt_d = [[0, 0] for _ in range(L)]
    for a in A:
        for i in range(L - 1, -1, -1):
            cnt_d[i][a & 1] += 1
            a >>= 1

    ans = 0
    lower_K = False
    for i, (d, (n_zero, n_one)) in enumerate(zip(K_d, cnt_d)):
        if n_zero <= n_one:
            n = 0
        else:
            n = 1
        
        if not lower_K:
            if d == 1 and n == 0:
                lower_K = True
            elif d == 0 and n == 1:
                n = 0

        num = cnt_d[i][n ^ 1]
        ans += num * 2 ** (L - 1 - i)

    print(ans)


def __starting_point():
    main()

__starting_point()
