#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def check(Elevator, takedown, left, right):  # 両開区間
    aida = right-left+1
    for i in range(2*left, 2*left+aida):
        i, seti = i, i+aida
        if Elevator[i][0] != -1:
            iperson = Elevator[i][0]
            if Elevator[i][1] != 'A':
                return False
            elif Elevator[seti][0] != -1:
                if Elevator[seti] != [iperson, 'B']:
                    return False
            if takedown[iperson][1] != -1:
                if takedown[iperson][1] != seti:
                    return False
        if Elevator[seti][0] != -1:
            iperson = Elevator[seti][0]
            if Elevator[seti][1] != 'B':
                return False
            if takedown[iperson][0] != -1:
                if takedown[iperson][0] != i:
                    return False
    return True


def main():
    n = int(input())
    Elevator = [[-1, -1] for i in range(2*n)]
    takedown = [[-1, -1] for i in range(n)]
    for i in range(n):
        # print(Elevator)
        # print(takedown)
        a, b = list(map(int, input().split()))
        if a != -1:
            a -= 1
            if Elevator[a][0] != -1:
                print('No')
                return
            Elevator[a] = [i, 'A']
            takedown[i][0] = a
        if b != -1:
            b -= 1
            if Elevator[b][0] != -1:
                print('No')
                return
            Elevator[b] = [i, 'B']
            takedown[i][1] = b
            if a >= b:
                print('No')
                return
    dp = [False]*(n+1)
    dp[-1] = True
    for i in range(n):
        for j in range(i+1):
            if dp[j-1]:
                if check(Elevator, takedown, j, i):
                    dp[i] = True
                    break
    #print(dp)
    print(('Yes' if dp[-2] else 'No'))


def __starting_point():
    main()

__starting_point()
