#	!/bin/env python3
#	coding: UTF-8


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology and Management,Gwalior

#	Question Link
#	https://codeforces.com/problemset/problem/234/C
#

# ///==========Libraries, Constants and Functions=============///


import sys

inf = float("inf")
mod = 1000000007
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()

# ///==========MAIN=============///


def __starting_point():
    n = int(input())
    arr = get_array()
    count_f = [0] * (n + 2)
    for i in range(1, n + 1):
        x = 0
        if arr[i - 1] >= 0:
            x = 1
        count_f[i] = count_f[i - 1] + x

    count_b = [0] * (n + 2)
    for i in range(n, 0, -1):
        x = 0
        if arr[i - 1] <= 0:
            x = 1
        count_b[i] = count_b[i + 1] + x

    ans = n
    for i in range(1, n):
        if count_f[i] + count_b[i + 1] < ans:
            ans = count_f[i] + count_b[i + 1]
    print(ans)


__starting_point()
