p, q = list(map(int, input().split()))
n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    p, q = q, p - A[i] * q

if p != 0 and q == 0:
    print('YES')
else:
    print('NO')
