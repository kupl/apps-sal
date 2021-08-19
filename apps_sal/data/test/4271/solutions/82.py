n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
sumB = sum(B)
cnt = []
for i in range(n - 1):
    if A[i] + 1 == A[i + 1]:
        cnt.append(A[i] - 1)
sumC = 0
for i in cnt:
    sumC += C[i]
print(sumB + sumC)
