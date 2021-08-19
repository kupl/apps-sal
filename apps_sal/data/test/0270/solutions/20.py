N, M = list(map(int, input().split()))
passages = [[] for i in range(N - 1)]
for i in range(M):
    s, t = list(map(int, input().split()))
    passages[s - 1].append(t - 1)

prob = [0] * N
prob[0] = 1
for n, dest in enumerate(passages):
    for d in dest:
        prob[d] += prob[n] / len(dest)

# no blocking
E = [0] * N
for n, dest in list(enumerate(passages))[::-1]:
    E[n] = sum(E[d] for d in dest) / len(dest) + 1

min_E = E[0]

# with blocking
for n, dest in enumerate(passages):
    if len(dest) == 1:
        continue
    new_E = ((E[n] - 1) * len(dest) - max(E[d] for d in dest)) / (len(dest) - 1) + 1
    min_E = min(min_E, E[0] - (E[n] - new_E) * prob[n])

print(min_E)
