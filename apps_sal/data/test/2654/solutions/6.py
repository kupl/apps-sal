import collections
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    (a, b) = map(int, input().split())
    A[i] = a
    B[i] = b
A.sort()
B.sort()
(N_q, N_mod) = divmod(N, 2)
if N_mod == 1:
    ans = B[N_q] - A[N_q] + 1
else:
    ans = B[N_q - 1] - A[N_q - 1] + B[N_q] - A[N_q] + 1
print(ans)
