n = int(input())
P = list(map(int, input().rstrip().split(' ')))
A = [i + 1 for i in range(n)]
B = [1 for i in range(n)]
stack = []
isOK = True
for (i, a) in enumerate(A):
    if isOK == False:
        break
    p = P[i]
    j = p - 1
    while i + 1 <= j:
        if B[j] < 0:
            isOK = False
            break
        stack.append(j)
        B[j] -= 1
        (A[j - 1], A[j]) = (A[j], A[j - 1])
        j -= 1
B[0] = 0
for i in range(n):
    a = A[i]
    b = B[i]
    p = P[i]
    if a != p or b != 0:
        isOK = False
if isOK:
    for i in range(n - 1):
        print(stack.pop())
else:
    print(-1)
