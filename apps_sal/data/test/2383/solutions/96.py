# coding: utf-8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = -1
    tmp = 1
    flg = False

    for a in A:
        if a == tmp:
            tmp += 1
            flg = True

    if flg:
        ans = N - tmp + 1

    print(ans)

def __starting_point():
    main()

__starting_point()
