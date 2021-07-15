#!/usr/bin/env python3

def II(): return int(input())
def MII(): return list(map(int, input().split()))
def LII(): return list(map(int, input().split()))

def main():
    N = II()

    ans = 0
    for i in range(1, N+1, 2):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 8:
            ans += 1

    print(ans)


def __starting_point():
    main()

__starting_point()
