import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
mod = 998244353
INIT = dict()
LAST = dict()
for i in range(n):
    if INIT.get(A[i]) == None:
        INIT[A[i]] = i
    LAST[A[i]] = i
ANS = 0
NOW = 0
i = 0
while i < n:
    NOW = LAST[A[i]]
    while i < n and i <= NOW:
        if LAST[A[i]] > NOW:
            NOW = LAST[A[i]]
        i += 1
    if i == n:
        break
    else:
        ANS += 1
print(pow(2, ANS, mod))
