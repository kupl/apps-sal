n = int(input())
A = input().split()
for i in range(0, n):
    A[i] = int(A[i])
if n == 1 or (n == 2 and A[0] == A[1]):
    print(-1)
else:
    minimum = min(A)
    for i in range(0, n):
        if A[i] == minimum:
            print(1)
            print(i + 1)
            break
