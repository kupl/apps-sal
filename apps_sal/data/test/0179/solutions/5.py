import sys
input = sys.stdin.readline

n, x, pos = list(map(int, input().split()))
mod = 10**9 + 7

ANS = [0] * n

left = 0
right = n

while left < right:
    # print(left,right)
    middle = (left + right) // 2
    if pos >= middle:
        ANS[middle] = -1
        left = middle + 1
    else:
        ANS[middle] = 1
        right = middle

ANS[pos] = 9
# print(ANS)

P = ANS.count(1)
M = ANS.count(-1)
MINUS = x - 1
PLUS = n - x

A = 1
for i in range(P):
    A = A * PLUS % mod
    PLUS -= 1

# print(A)
for i in range(M):
    A = A * MINUS % mod
    MINUS -= 1

# print(A)

for i in range(1, n - P - M):
    A = A * i % mod

print(A)
