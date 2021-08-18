'''
Author:    krishna
Created:   Fri Jan 19 20:39:10 2018 IST
File Name: b.py
USAGE:
      b.py
Description:

'''
import sys
import os


def main():
    '''
    The Main
    '''
    n, k = list(map(int, sys.stdin.readline().split()))

    x = bin(n)[2:]
    if x.count('1') > k:
        print("No")
        return

    ans = [0] * (10 ** 5)

    val = len(x) - 1
    idx = len(x) - 1
    cnt = 0
    for i in x:
        if (int(i)):
            ans[val] = 1
            cnt += 1

        val -= 1

    for i in range(k - cnt):
        ans[idx] -= 1
        ans[idx - 1] += 2
        if (ans[idx] == 0):
            idx -= 1

    maxIdx = idx - 1
    minIdx = idx - 1
    nonZeroIdx = idx - 1
    while (1):
        if (minIdx < 0) and (ans[minIdx] == 0):
            minIdx += 1
            break
        if ans[minIdx]:
            nonZeroIdx = minIdx
        minIdx -= 1

    minIdx = nonZeroIdx

    while (1):
        if (
            (ans[maxIdx] > 2)
            or ((ans[maxIdx] == 2 ) and (maxIdx != minIdx))
        ):
            ans[minIdx] -= 1
            ans[minIdx - 1] += 2
            ans[maxIdx] -= 2
            ans[maxIdx + 1] += 1
            minIdx -= 1
        else:
            maxIdx -= 1

        if (maxIdx <= minIdx):
            break

    print("Yes")
    x = []
    while (1):
        for i in range(ans[idx]):
            x.append(idx)
        idx -= 1
        if (idx < 0) and (ans[idx] == 0):
            break

    print(" ".join(map(str, x)))


def __starting_point():
    main()


__starting_point()
