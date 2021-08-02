import math


def main():
    N = int(input())
    A = [int(a) for a in input().split(" ")]
    B = [0] * N
    if N == 1:
        if A[0] == 1:
            print((1))
            print((1))
        else:
            print((0))
        return 0
    for i in range(1, N):
        for j in range(math.ceil(N / (i + 1)), math.floor(N / i) + 1):
            ball = 0
            for k in range(2 * j, N + 1, j):
                ball += B[k - 1]
            B[j - 1] = (ball % 2 + A[j - 1]) % 2
    ans = [str(x + 1) for x, v in enumerate(B) if v == 1]
    print((len(ans)))
    if len(ans) > 0:
        print((" ".join(ans)))


main()
