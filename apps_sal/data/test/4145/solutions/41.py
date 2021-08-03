# Original Submission At: https://atcoder.jp/contests/abc149/submissions/16823042
import sys
sys.setrecursionlimit(1000000)

x = int(input())


def prime_check(num, count):
    if (num % count) != 0:
        if num <= count**2:
            print(num)
        else:
            prime_check(num, count + 1)
    else:
        prime_check(num + 1, 2)


if x == 2:
    print((2))
else:
    prime_check(x, 2)
