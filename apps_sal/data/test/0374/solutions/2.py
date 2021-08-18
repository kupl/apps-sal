import sys
input = sys.stdin.readline

n = int(input())
P = [1] + list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(n):
    P[i] -= 1

Y = [1] * n
for i in range(n):
    Y[P[i]] = 0


for i in range(n - 1, 0, -1):
    Y[P[i]] += Y[i]

S = [a for a in A]
for i in range(n - 1, 0, -1):
    S[P[i]] += S[i]

OK = sum(A)
NG = -1

while OK - NG > 1:
    mid = (OK + NG) // 2

    for i in range(n):
        if Y[i] * mid < S[i]:
            NG = mid
            break
    else:
        OK = mid

print(OK)
