a = int(input())
A = [0] * a
for q in range(a):
    B = list(map(float, input().split()))
    for i in range(a):
        if B[i] == 1:
            A[q] = A[q] + 1
        elif B[i] == 2:
            A[i] = A[i] + 1
        elif B[i] == 3:
            A[q] = A[q] + 1
            A[i] = A[i] + 1
c = 0
C = ''
for i in range(a):
    if A[i] == 0:
        C = C + str(i + 1) + ' '
        c = c + 1
print(c)
if c != 0:
    print(C)
