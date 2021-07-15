N = int(input())
mod = 1000000007
from collections import defaultdict as dd
Y = dd(lambda:1)
for i in range(2, N+1):
    M = i
    for j in range(2,i+1):
        while M % j == 0:
            Y[j] += 1
            M //= j

def product(X):
    res = 1
    for x in X:
        res *= x
        res %= mod
    return res    

ans = product(list(Y.values()))
print(ans)

