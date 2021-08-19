S = input()
K = int(input())
N = len(S)
memo = []
for i in range(N):
    for d in range(1, min(K, N - i) + 1):
        memo.append(S[i:i + d])
print(sorted(set(memo))[K - 1])
