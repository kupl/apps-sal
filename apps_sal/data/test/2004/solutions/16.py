n = int(input())

A = []
B = []
for i in range(1, n + 1, 2):
    A.append(i)
for i in range(2, n + 1, 2):
    B.append(i)
if(len(A) < len(B)):
    A = A + B + A
else:
    A = B + A + B
print(len(A))
for i in A:
    print(i, end=' ')
