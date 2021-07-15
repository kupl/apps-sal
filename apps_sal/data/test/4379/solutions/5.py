from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
last = defaultdict(int)
D = {0: (0, 0)}
best = (0, 0)
for i, a in enumerate(A, start=1):
    last[a] = i
    last_a1 = last[a - 1]
    best_a1, _ = D[last_a1]
    D[i] = (1 + best_a1, last_a1)
    best = max(best, (1 + best_a1, i))

print(best[0])
rsseq = []
i = best[1]
while i != 0:
    rsseq.append(i)
    i = D[i][1]
print(' '.join(map(str, reversed(rsseq))))

