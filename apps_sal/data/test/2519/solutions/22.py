N, K = [int(s) for s in input().split(' ')]
P = [int(s) for s in input().split(' ')]
s = []
a = sum(P[0:K])
s.append(a)
for p0, p1 in zip(P, P[K:]):
    a = a - p0 + p1
    s.append(a)

print(((max(s) + K) / 2))
