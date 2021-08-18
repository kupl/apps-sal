

from sys import stdin

max_val = int(10e12)
min_val = int(-10e12)


def read_int(): return int(stdin.readline())
def read_ints(): return [int(x) for x in stdin.readline().split()]
def read_str(): return input()
def read_strs(): return [x for x in stdin.readline().split()]


limit = 110000
primes = [0, 0] + [1] * limit
for i in range(2, limit):
    if primes[i]:
        for j in range(i * i, limit, i):
            primes[j] = 0

u = limit
for i in reversed(range(limit)):
    if primes[i]:
        u = i
    primes[i] = u - i

n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]
maxs = 10 ** 10
for v in matrix:
    maxs = min(maxs, sum([primes[x] for x in v]))
for v in zip(*matrix):
    maxs = min(maxs, sum([primes[x] for x in v]))
print(maxs)
