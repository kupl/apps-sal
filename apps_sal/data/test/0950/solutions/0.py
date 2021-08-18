import math
import re
import itertools as it
def prime(n): return len([i for i in range(2, int(math.sqrt(n) + 1)) if n % i == 0]) == 0


def gcd(a, b): return gcd(b, a % b) if b else a
def fact(x): return x * fact(x - 1) if x else 1


def bino(n, k): return fact(n) / fact(k) / fact(n - k)
def fib11(n): return 1 if n < 2 else fib11(n - 1) + fib11(n - 2)


def fib01(n): return 0 if n == 0 else 1 if n == 1 else fib01(n - 1) + fib01(n - 2)
def sumofd(x): return x if x < 10 else sumofd(x // 10) + x % 10


n, m = map(int, input().split(' '))
a = []
dp = []
sc = st = sl = 1000000
for _ in range(n):
    a.append(input())
    c = t = l = 1000000
    for i in range(len(a[-1])):
        if a[-1][i] in '0123456789':
            c = min(c, i, len(a[-1]) - i)
        if a[-1][i] in '
        t = min(t, i, len(a[-1]) - i)
        if 'a' <= a[-1][i] <= 'z':
            l = min(l, i, len(a[-1]) - i)
    '''if c == t == 1000000 or c == l == 1000000 or l == t == 1000000:
		if c == t == 1000000:
			sl = 0
		if c == l == 1000000:
			st = 0
		if l == t == 1000000:
			sc = 0
		continue'''
    dp.append([c, t, l])
mm = 1000000
kk = it.permutations(list(range(n)), 3)
for i in kk:
    mm = min(mm, dp[i[0]][0] + dp[i[1]][1] + dp[i[2]][2])
print(mm)
