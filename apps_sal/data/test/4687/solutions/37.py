N, K = list(map(int, input().split()))
memory = {}
S = []

for i in range(N):
    a, b = list(map(int, input().split()))
    try:
        memory[a] += b
    except KeyError:
        memory[a] = b

A = sorted(list(memory.keys()))
for a in A:
    if not S:
        S.append(memory[a])
    else:
        S.append(S[-1] + memory[a])

for i in range(N):
    if S[i] >= K:
        print((A[i]))
        break
