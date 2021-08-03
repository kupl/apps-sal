# Never give up. You only get one life and a year. Go for it!
import sys
import math


n, k = list(map(int, input().split()))
A = [int(i) for i in input().split()]

A.sort()

l = 0
r = n - 1

while(l < r and k):
    temp = ((A[l + 1] - A[l]) * (l + 1) + (A[r] - A[r - 1]) * (n - r))
    if(k >= temp):
        k -= temp
        l += 1
        r -= 1

    else:
        ans = A[r] - A[l] - (k // (l + 1))
        print(ans)
        return


print(0)
