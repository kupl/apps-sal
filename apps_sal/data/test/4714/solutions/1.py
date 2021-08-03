A, B = list(map(str, input().split()))
La = [int(A[:3]), int(A[3:])]
Lb = [int(B[:3]), int(B[3:])]
L = 900 - (La[0] - 100) - (999 - Lb[0])
ch1 = int(A[1] + A[0])
ch2 = int(B[1] + B[0])
if Lb[1] < ch2:
    L -= 1
if ch1 < La[1]:
    L -= 1
print(L)
