from collections import Counter

N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

BC = [tuple([int(_) for _ in input().split()]) for _ in range(M)]

X = Counter(A)
for a in X:
    BC.append((X[a], a))
BC.sort(key=lambda x: x[1], reverse=True)

ans = 0
k = N
for b, c in BC:
    v = min(k, b)
    ans += v * c
    k -= v

print(ans)
