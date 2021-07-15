# coding: utf-8

def main():
    N, A, B = list(map(int, input().split()))
    quo = N // (A + B)
    rem = N % (A + B)

    if (rem > A): rem = A
    ans = quo * A + rem

    print(ans)

def __starting_point():
    main()

__starting_point()
