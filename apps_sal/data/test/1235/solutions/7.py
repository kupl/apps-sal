# Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open('input.txt', 'r')
MOD = 998244353
sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(max(a), max(b))
