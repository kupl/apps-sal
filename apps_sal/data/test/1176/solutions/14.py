#!/usr/bin/env python3

INF = 10**9 + 1

def solve(n,a):
    ans = 0
    minusCount = 0
    minimumNum = INF
    lst = []
    for i in range(n):
        if a[i] < 0:
            minusCount += 1
        ans += abs(a[i])
        minimumNum = min(minimumNum,abs(a[i]))
    if minusCount % 2 == 0:
        pass
    else:
        ans -= minimumNum*2
    return ans


def main():
    N = int(input())
    a = list(map(int,input().split()))
    print((solve(N,a)))

def __starting_point():
    main()

__starting_point()
