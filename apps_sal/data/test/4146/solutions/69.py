import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal
import functools


def get_primenumber(number):
    prime_list = []
    search_list = list(range(2, number + 1))
    while search_list[0] <= math.sqrt(number):
        head_num = search_list.pop(0)
        prime_list.append(head_num)
        search_list = [num for num in search_list if num % head_num != 0]
    prime_list.extend(search_list)
    return prime_list


def factrization_prime(number):
    factor = {}
    div = 2
    s = math.sqrt(number)
    while div < s:
        div_cnt = 0
        while number % div == 0:
            div_cnt += 1
            number //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if number > 1:
        factor[number] = 1
    return factor


def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int, input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int, input().split()))
def lcm(a, b): return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 6)
mod = 10**9 + 7
cnt = 0
ans = 0
num = []
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

n = k()
V = l()

odd = [i for i in V[::2]]
even = [i for i in V[1::2]]

O = Counter(odd).most_common()
E = Counter(even).most_common()
a = len(V) // 2

if O[0][0] == E[0][0]:
    if O[0][1] == a:
        print(a)
    else:
        print(min((a - O[0][1]) + (a - E[1][1]), (a - O[1][1]) + (a - E[0][1])))
else:
    print((a - O[0][1]) + (a - E[0][1]))
