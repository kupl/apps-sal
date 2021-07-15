import queue
import numpy as np
import math

n = int(input())
A = list(map(int, input().split()))
A = np.array(A,np.int64)
ans = 0

for i in range(60 + 1):
    a = (A >> i) & 1
    count1 = np.count_nonzero(a)
    count0 = len(A) - count1
    ans += count1*count0 * pow(2, i)
    ans%=1000000007

print(ans)
