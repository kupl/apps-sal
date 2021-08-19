import copy
N = int(input())
A = list(map(int, input().split()))
A_copy = copy.deepcopy(A)
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if A[i] <= B[i]:
        B[i] -= A[i]
        A[i] = 0
        if B[i] > 0:
            if A[i + 1] <= B[i]:
                A[i + 1] = 0
                B[i] -= A[i + 1]
            elif A[i + 1] > B[i]:
                A[i + 1] -= B[i]
                B[i] = 0
    elif A[i] > B[i]:
        A[i] -= B[i]
        B[i] = 0
ans = sum(A_copy) - sum(A)
print(ans)
