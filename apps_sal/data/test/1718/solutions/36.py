# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, k = list(map(int, readline().split()))
*a, = list(map(int, readline().split()))

ans = 1 + (n - 1 - 1) // (k - 1)
print(ans)
