
import sys

n, f = list(map(int, sys.stdin.readline().split()))
increments = []
without_increments = 0
for __ in range(n):
    prod, cust = list(map(int, sys.stdin.readline().split()))
    increments.append(max(0, min(prod * 2, cust) - prod))
    without_increments += min(prod, cust)
print(without_increments + sum(sorted(increments, reverse=True)[:f]))
