S = input()
N = len(S)
K = int(input())
ttl = []
for i in range(N):
    for j in range(N - i):
        ttl.append(S[j:j + i + 1])
    if i > K:
        break
ttl = sorted(list(set(ttl)))
print(ttl[K - 1])
