import math
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
# cnt=A.index(1)+1
print((math.ceil((n - 1) / (k - 1))))
