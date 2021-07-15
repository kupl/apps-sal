N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = sum(B)

for i in range(N):
    if B[N-1-i] >= A[N-i]:
        B[N-1-i] -= A[N-i]
        A[N-i] = 0
    else:
        A[N-i] -= B[N-i-1]
        B[N-i-1] = 0

    if B[N-1-i] > 0:
        if A[N-1-i] > B[N-1-i]:
            A[N-1-i] -= B[N-1-i]
            B[N-1-i] = 0
        else:
            B[N-1-i] -= A[N-1-i]
            A[N-1-i] = 0
    # print(A)
    # print(B)
    # print("=============")

print((ans-sum(B)))

