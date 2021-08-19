from sys import stdin, stdout
import math
import copy
(N, L, R) = [int(x) for x in stdin.readline().split()]
mini = 0
num = 1
for i in range(L):
    mini += num
    num *= 2
maxi = 0
num = 1
for i in range(R):
    maxi += num
    num *= 2
maxi += (N - R) * (num // 2)
mini += N - L
print(mini, maxi)
