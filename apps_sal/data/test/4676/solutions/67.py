A = list(input())
B = list(input())
x = A[0] + B[0]
for i in range(1, len(B)):
    x = x + A[i] + B[i]
if len(A) > len(B):
    x = x + A[-1]
print(x)
