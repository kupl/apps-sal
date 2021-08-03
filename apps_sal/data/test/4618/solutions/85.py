S = input()
N = len(S)
K = int(input())
cnt = {i: [] for i in range(N)}
for i in range(N):
    for j in range(N - i):
        s = S[j:j + i + 1]
        l = len(s)
        if s not in cnt[l - 1]:
            cnt[l - 1].append(s)
    if i > K:
        break
ttl = []
for k, v in cnt.items():
    ttl.extend(v)
ttl.sort()
print(ttl[K - 1])
