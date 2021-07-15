#!/usr/bin/env python3

def II(): return int(input())
def MII(): return list(map(int, input().split()))
def LII(): return list(map(int, input().split()))

def main():
    A, B, C, X, Y = MII()

    ans = A * X + B * Y
    for i in range(0, max(X, Y)+1):
        ans = min(ans, max(A * (X - i), 0) + max(B * (Y - i), 0) + C * 2 * i)

    print(ans)

def __starting_point():
    main()

__starting_point()
