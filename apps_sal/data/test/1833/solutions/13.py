#	!/bin/env python3
#	coding: UTF-8


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology and Management,Gwalior

#	Question Link
#	https://codeforces.com/problemset/problem/1061/C
#

# ///==========Libraries, Constants and Functions=============///


import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()

# ///==========MAIN=============///


def factors(n):
    curr = []
    j = 1
    while j*j <= n:
        if n % j == 0:
            curr.append(j)
            if j != n//j:
                curr.append(n//j)
        j += 1
    curr.sort(reverse=True)
    return curr


def main():
    n = int(input())
    dp = [0 for _ in range(1000005)]
    arr = get_array()
    for i in range(n):
        x = factors(arr[i])
        for j in range(len(x)):
            if x[j] == 1:
                continue
            dp[x[j]] += dp[x[j]-1]
            dp[x[j]] %= mod
        dp[1] += 1
    ans = 0
    for i in range(1000005):
        ans += dp[i]
    ans %= mod
    print(ans)


def __starting_point():
    main()

__starting_point()
