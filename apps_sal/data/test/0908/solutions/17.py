n = int(input())
C = tuple(map(int, input().split()))
A = tuple(input()for _ in range(n))
B = tuple(A[i][::-1]for i in range(n))
INF = 1 << 47
a = 0
b = C[0]
for i in range(1, n):
    c = INF if B[i] < A[i - 1]else C[i] + a
    if A[i] < A[i - 1]:
        a = INF
    if B[i - 1] <= A[i]:
        a = min(a, b)
    if B[i - 1] <= B[i]:
        c = min(c, C[i] + b)
    b = c
    if INF <= a and INF <= b:
        break
c = min(a, b)
print(c if INF > c else-1)
