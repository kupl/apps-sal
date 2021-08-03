N = int(input())
A = sorted(map(int, input().split()), reverse=True)
if N % 2 == 1:
    print((sum(A[0:(N - 1) // 2]) + sum(A[1:(N + 1) // 2])))
else:
    print((sum(A[0:N // 2]) + sum(A[1:N // 2])))
