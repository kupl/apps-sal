import sys
import collections


def input():
    return sys.stdin.readline().rstrip()


def split_input():
    return [int(i) for i in input().split()]


tests = int(input())

for _ in range(tests):
    n, k, l = split_input()
    d = split_input()
    newd = [l - i for i in d]
    if min(newd) < 0:
        print("No")
        continue
    kvalue = newd[0]
    dec = True
    ans = True
    i = 1
    while i < n:
        if newd[i] < 0:
            ans = False
            break
        if newd[i] >= k:
            if i < n - 1:
                kvalue = newd[i + 1]
                dec = True
                i += 2
                continue
        if kvalue == 0:
            dec = False
        if dec:
            if newd[i] < kvalue:
                kvalue = newd[i]
            else:
                kvalue -= 1
        else:
            if newd[i] <= kvalue:
                ans = False
                break
            else:
                kvalue += 1
        i += 1
    if ans:
        print("Yes")
    else:
        print("No")
