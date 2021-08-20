import sys
import math
import collections
import itertools
input = sys.stdin.readline
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
maxA = max(A)
binK = bin(max(maxA, K))[2:]
num_one = [0] * len(binK)
for k in range(len(binK)):
    for a in A:
        num_one[len(binK) - k - 1] += a >> k & 1
ans = 0
flag = False
for k in range(len(binK)):
    if flag:
        if num_one[k] > N - num_one[k]:
            ans += pow(2, len(binK) - k - 1) * num_one[k]
        else:
            ans += pow(2, len(binK) - k - 1) * (N - num_one[k])
    elif K >> len(binK) - k - 1 & 1:
        if num_one[k] > N - num_one[k]:
            flag = True
            ans += pow(2, len(binK) - k - 1) * num_one[k]
        else:
            ans += pow(2, len(binK) - k - 1) * (N - num_one[k])
    else:
        ans += pow(2, len(binK) - k - 1) * num_one[k]
print(ans)
