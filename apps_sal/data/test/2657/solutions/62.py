N = int(input())
A = list(map(int,input().split()))

A.sort()
max_el = A[-1]
median = max_el//2
import bisect
median_ind = bisect.bisect_left(A,median)

if median_ind == 0:
    print(A[-1],A[0])
    return
if median_ind == N-1:
    print(A[-1],A[-2])
    return

abs_right = abs(A[median_ind]-median)
abs_left = abs(A[median_ind-1]-median)

if abs_right>abs_left:
    print(A[-1],A[median_ind-1])
    return

print(A[-1], A[median_ind])
