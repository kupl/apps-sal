# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import collections

N = int(input())
#s = input()
#N,Q = [int(x) for x in stdin.readline().split()]

res = 0
for m in range(2, N + 1):
    d = N // m
    d -= 1
    res += d * m

    if d == 0:
        break

print(4 * res)
