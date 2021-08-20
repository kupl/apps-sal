from fractions import gcd
import math


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft


def main():
    q = int(input())
    for i in range(q):
        (n, m) = list(map(int, input().split()))
        a = [input() for i in range(n)]
        h = 0
        h_a = []
        for i in range(m):
            tmp = 0
            for j in range(n):
                if a[j][i] == '*':
                    tmp += 1
            if h < tmp:
                h = tmp
                h_a = [i]
            if h == tmp:
                h_a.append(i)
        w = 0
        w_a = []
        for i in range(n):
            tmp = len([i for i in a[i] if i == '*'])
            if w < tmp:
                w = tmp
                w_a = [i]
            if w == tmp:
                w_a.append(i)
        flag = 0
        for i in h_a:
            for j in w_a:
                if a[j][i] == '.':
                    flag = 1
                    break
        print(n + m - h - w - flag)


main()
