N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = sum(A)

for i in range(N):
    if B[i] <= A[i]:
        A[i] -= B[i]
    elif A[i] < B[i] <= A[i] + A[i + 1]:
        B[i] -= A[i]
        A[i] = 0
        A[i + 1] -= B[i]
    else:
        A[i] = 0
        A[i + 1] = 0

S_ = sum(A)

print(S - S_)
