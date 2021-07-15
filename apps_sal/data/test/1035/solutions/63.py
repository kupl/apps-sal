import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def get_primenumber(number):#素数列挙
    prime_list = []
    search_list = list(range(2,number+1))
    #search_listの先頭の値が√nの値を超えたら終了
    while search_list[0] <= math.sqrt(number):
      #search_listの先頭の値が√nの値を超えたら終了
      #search_listの先頭をprime_listに入れて、先頭をリストに追加して削除
        head_num = search_list.pop(0)
        prime_list.append(head_num)
        #head_numの倍数を除去
        search_list = [num for num in search_list if num % head_num != 0]
    #prime_listにsearch_listを結合
    prime_list.extend(search_list)
    return prime_list
def factrization_prime(number):#素因数分解
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
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 6)
mod = 10**9+7
cnt = 0
ans = 0
num = []
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

a,b = I()
prime_a = factrization_prime(a)
prime_b = factrization_prime(b)

for i in prime_a.keys():
    if i in prime_b.keys():
        cnt += 1

print(cnt+1)
