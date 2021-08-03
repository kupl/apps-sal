n = int(input())
C = []
A = [int(input()) for i in range(n)]
A.sort()
B = A
for x in range(n):
    C.append(A[x] * B[n - x - 1])
a = sum(C)
print(a % 10007)
