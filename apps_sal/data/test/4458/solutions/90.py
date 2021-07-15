# coding: utf-8

def main():
    N = int(input())
    tmp = 200001
    ans = 0
    A = list(map(int, input().split()))

    for a in A:
        if a < tmp:
            ans += 1
            tmp = a

    print(ans)

def __starting_point():
    main()

__starting_point()
