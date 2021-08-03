from itertools import accumulate
def inpl(): return list(map(int, input().split()))


N, M = inpl()
A = [a - 1 for a in inpl()]
S = [0] * (M + 1)
T = [0] * (M + 1)

tmp = 0
for i in range(N - 1):
    T[A[i + 1]] += (A[i + 1] + M - A[i]) % M - 1
    if A[i] < A[i + 1]:
        S[A[i] + 1] += 1
        S[A[i + 1]] -= 1
        tmp += A[i + 1] - A[i]
    else:
        tmp += A[i + 1] + 1
        S[0] += 1
        S[A[i + 1]] -= 1
        S[A[i] + 1] += 1

S = list(accumulate(S))
ans = tmp * 1
for i in range(1, M):
    tmp2 = tmp + T[i - 1] - S[i - 1]
    ans = min(ans, tmp2)
    tmp = tmp2
print(ans)
