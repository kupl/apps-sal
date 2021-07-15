3

from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
m = int(input())
Q = list(map(int, input().split()))

sum_A = list(A)
for i in range(1, n):
    sum_A[i] += sum_A[i-1]
for q in Q:
    print(bisect_left(sum_A, q) + 1)
