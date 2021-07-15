N = int(input())
*A, = map(int, input().split())
A = [0] + A + [0]
S = 0
for i in range(1, N+2):
    S += abs(A[i] - A[i-1])
for i in range(1, N+1):
    new = abs(A[i-1] - A[i+1])
    pre_to_now = abs(A[i-1] - A[i])
    now_to_next = abs(A[i] - A[i+1])
    print(S - pre_to_now - now_to_next + new)
