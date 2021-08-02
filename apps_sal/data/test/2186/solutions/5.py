from collections import defaultdict
from math import ceil, floor
import sys

memory = set()
mod = 1000000000000000003
p = 3


def hash_(s):
    pp = p
    result = 0
    for ch in s:
        result += pp * (ord(ch) - ord('a') - 1)
        pp = (pp * p) % mod;
        result %= mod
    return result % mod;


def find(q):
    hash_0 = hash_(q)
    k = len(q)
    pw = p
    ext = 0
    for j in range(len(q)):
        for ch in 'abc':
            if ch != q[j]:
                if ((hash_0 % mod + ((ord(ch) - ord(q[j])) * pw) % mod) % mod) in memory:
                    sys.stdout.write('YES\n')
                    ext = 1
                    break
        if ext:
            break
        pw = (p * pw) % mod;
    if not ext:
        sys.stdout.write('NO\n')


def main():
    n, m = [int(i) for i in input().split()]
    for i in range(n):
        memory.add(hash_(sys.stdin.readline().strip()))
    for i in range(m):
        find(sys.stdin.readline().strip())


def __starting_point():
    ##sys.stdin = open("in.txt",'r')
    ##sys.stdout = open("out.txt",'w')
    main()
    # sys.stdin.close()
    # sys.stdout.close()


__starting_point()
