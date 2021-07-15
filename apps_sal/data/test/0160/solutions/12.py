from itertools import accumulate
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
M = sum(A)

# 答えの候補を列挙
ans_candidates = []
for n in range(1, int(M ** 0.5) + 1):
    if M % n == 0:
        ans_candidates.append(n)
        ans_candidates.append(M // n)


ans = 0
for X in ans_candidates:
    A_mod = sorted([a % X for a in A])
    U = [X - a for a in A_mod]
    D = [-a for a in A_mod]  # わかりやすいので

    U = list(accumulate(U))
    D = list(accumulate(D))

    for i in range(N):
        if -D[i] > K:
            break

        if -D[i] == (U[-1] - U[i]):
            ans = max(ans, X)
            break

print(ans)

