#!/usr/bin/env python3

import sys
import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)


def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    # inf = 2 ** 64 - 1               # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return list(map(int, input().split()))
    def mi_0():  return [int(x)-1 for x in input().split()]
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list([int(x)-1 for x in input().split()])
    def li():    return list(input())
    
        
    class Eratos:
        def __init__(self, num):
            assert(num >= 1)
            self.table_max = num
            # self.table[i] は i が素数かどうかを示す (bool)
            self.table = [False if i == 0 or i == 1 else True for i in range(num+1)]
            for i in range(2, int(math.sqrt(num)) + 1):
                if self.table[i]:
                    for j in range(i ** 2, num + 1, i):    # i**2 からスタートすることで定数倍高速化できる
                        self.table[j] = False
            # self.table_max 以下の素数を列挙したリスト
            self.prime_numbers = [2] if self.table_max >= 2 else []
            for i in range(3, self.table_max + 1, 2):
                if self.table[i]:
                    self.prime_numbers.append(i)
        
        def is_prime(self, num):
            """
            >>> e = Eratos(100)
            >>> [i for i in range(1, 101) if e.is_prime(i)]
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            """
            assert(num >= 1)
            if num > self.table_max:
                raise ValueError('Eratos.is_prime(): exceed table_max({}). got {}'.format(self.table_max, num))
            return self.table[num]
        
        def prime_factorize(self, num):
            """
            >>> e = Eratos(10000)
            >>> e.prime_factorize(6552)
            {2: 3, 3: 2, 7: 1, 13: 1}
            """
            assert(num >= 1)
            if int(math.sqrt(num)) > self.table_max:
                raise ValueError('Eratos.prime_factorize(): exceed prime table size. got {}'.format(num))
            factorized_dict = dict()    # 素因数分解の結果を記録する辞書
            candidate_prime_numbers = [i for i in range(2, int(math.sqrt(num)) + 1) if self.is_prime(i)]
            # n について、√n 以下の素数で割り続けると最後には 1 or 素数となる
            # 背理法を考えれば自明 (残された数が √n より上の素数の積であると仮定。これは自明に n を超えるため矛盾)
            for p in candidate_prime_numbers:
                # これ以上調査は無意味
                if num == 1:
                    break
                while num % p == 0:
                    num //= p
                    try:
                        factorized_dict[p]
                    except KeyError:
                        factorized_dict[p] = 0
                    finally:
                        factorized_dict[p] += 1
            if num != 1:
                factorized_dict[num] = 1
            return factorized_dict
    

    n, m = mi()
    eratos = Eratos(max(int(math.sqrt(m)), n))
    d = eratos.prime_factorize(m)
    # print(d)

    FACT = [1] * (n + int(math.log2(m)) + 1)
    for i in range(2, n + int(math.log2(m)) + 1):
        FACT[i] = (FACT[i-1] * i) % mod
    
    def comb(n, r, m):
        numerator = FACT[n]
        denominator = pow(FACT[n-r] * FACT[r], m - 2, m)
        return (numerator * denominator) % m

    ans = 1
    for _, k in list(d.items()):
        ans = (ans * comb(k + n - 1, k, mod)) % mod
    print(ans)


def __starting_point():
    main()

__starting_point()
