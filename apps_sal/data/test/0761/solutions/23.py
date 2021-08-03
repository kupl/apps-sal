import sys
n = int(input())
A = list(map(int, input().split()))

if n == 1:
    print(A[0])
    return

suma = 0
mine = 1000000001
d = False

for i in range(0, n):
    mine = min(mine, abs(A[i]))
    suma += abs(A[i])
    if i > 0 and ((A[i] >= 0 and A[i - 1] < 0) or (A[i] < 0 and A[i - 1] >= 0)):
        d = True

if d:
    print(suma)
else:
    print(suma - 2 * mine)
