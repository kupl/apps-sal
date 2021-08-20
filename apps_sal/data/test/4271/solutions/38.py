n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
res = 0
for i in range(n - 1):
    res += B[i]
    if A[i] + 1 == A[i + 1]:
        res += C[A[i] - 1]
print(res + B[-1])
