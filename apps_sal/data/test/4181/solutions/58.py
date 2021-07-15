N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum_ = 0
for i in range(N):
    if A[i] >= B[i]:
        sum_ += B[i]
        A[i] -= B[i]
    else:
        sum_ += A[i]
        B[i] -= A[i]
        if A[i+1] >= B[i]:
            sum_ += B[i]
            A[i+1] -= B[i]
        else:
            sum_ += A[i+1]
            A[i+1] = 0
print(sum_)

