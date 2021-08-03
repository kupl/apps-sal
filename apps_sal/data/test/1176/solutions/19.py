N, A = int(input()), list(map(int, input().split()))

zero = 0
minus = 0
for i in range(N):
    if A[i] < 0:
        minus += 1
    elif A[i] == 0:
        zero = 1
    A[i] = abs(A[i])

if (minus % 2 == 0) | (zero == 1):
    print(sum(A))
else:
    print(sum(A) - 2 * min(A))
