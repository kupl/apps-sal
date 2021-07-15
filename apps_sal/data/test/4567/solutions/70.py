# coding: utf-8


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = sum(A)

    if ans % 10 == 0:
        tmp = 0
        for i in range(N):
            if A[i] % 10 != 0:
                tmp = max(tmp, ans - A[i])
        if tmp % 10 == 0:
            ans = 0
        else:
            ans = tmp

    print(ans)

def __starting_point():
    main()

__starting_point()
