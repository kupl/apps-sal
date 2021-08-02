import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = max(A)
while not l + 1 == r:
    x = (r + l) // 2
    k = 0
    for a in A:
        k += math.ceil(a / x) - 1
    if k <= K:
        r = x
    else:
        l = x
print(r)
