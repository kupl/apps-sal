n = int(input())
A = []
B = []
for i in range(n):
    x = [int(i) for i in input().split()]
    A.append(x[0])
    B.append(x[1])
A = sorted(A)
B = sorted(B)
if n % 2:
    med_A = A[n // 2]
    med_B = B[n // 2]
    print(abs(med_A - med_B) + 1)
else:
    med_A = A[(n - 1) // 2] + A[n // 2]
    med_B = B[(n - 1) // 2] + B[n // 2]
    print(abs(med_A - med_B) + 1)
