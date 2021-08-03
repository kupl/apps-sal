N = int(input())
A = list(map(int, input().split()))
zero = False
minus = 0
for i in range(N):
    if A[i] < 0:
        A[i] *= -1
        minus = 1 - minus
    elif A[i] == 0:
        zero = True

A.sort(reverse=True)
if zero == True:
    print((sum(A)))
else:
    if minus == 0:
        print((sum(A)))
    else:
        print((sum(A[0:N - 1]) - A[-1]))
