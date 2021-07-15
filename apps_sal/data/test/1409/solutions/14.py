import sys

f = sys.stdin
n, k, = list(map(int, f.readline().strip().split()))

A = [int(u) for u in f.readline().strip().split()]


m = 0
for u in A:
    if u+k<=5:
       m += 1

print(m//3)

