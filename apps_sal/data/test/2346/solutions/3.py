a = int(input())
A = [0] * (a + 2)
B = [0] * a
for i in range(a):
    (q, w) = map(int, input().split())
    A[i] += 1
    A[q - 1] += 1
    if w == 1:
        B[q - 1] += 1
        B[i] += 1
C = []
for i in range(a):
    if A[i] == B[i]:
        C.append(i + 1)
if len(C) == 0:
    print(-1)
else:
    print(*C)
