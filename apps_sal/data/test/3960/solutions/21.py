#	!/bin/env python3
#	encoding: UTF-8


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology and Management,Gwalior

#	Question Link
#	https://codeforces.com/problemset/problem/788/A
#

# ///==========Libraries, Constants and Functions=============///


import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()

# ///==========MAIN=============///


def main():
    n = int(input())
    arr = get_array()
    ans = 0
    prefix_odd = [0]*n
    for i in range(n-1):
        prefix_odd[i] = abs(arr[i+1]-arr[i])*pow(-1, i)
    prefix_even = [0]*n
    for i in range(n-1):
        prefix_even[i] = abs(arr[i+1]-arr[i])*pow(-1, i+1)

    curr_mx, mx = prefix_odd[0], prefix_odd[0]
    for i in range(1, n):
        curr_mx = max(prefix_odd[i], prefix_odd[i]+curr_mx)
        mx = max(curr_mx, mx)

    curr_mx = prefix_even[0]
    for i in range(1, n):
        curr_mx = max(prefix_even[i], prefix_even[i]+curr_mx)
        mx = max(curr_mx, mx)
    print(mx)


def __starting_point():
    main()

__starting_point()
