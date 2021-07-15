from bisect import *
n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1): a[i + 1] += a[i]
input()
for i in map(int, input().split()): print(bisect_left(a, i) + 1)
