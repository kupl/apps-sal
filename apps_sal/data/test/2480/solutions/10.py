from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for i in range(N):
    S.append((S[-1] + A[i] - 1) % K)

D = defaultdict(int)

count = 0

for i in range(N + 1):
    count += D[S[i]]
    D[S[i]] += 1
    if i - K + 1 >= 0:
        D[S[i - K + 1]] -= 1

print(count)
