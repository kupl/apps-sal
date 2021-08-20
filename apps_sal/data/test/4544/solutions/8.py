(N, *A) = map(int, open(0).read().split())
L = [0 for i in range(int(100000.0) + 1)]
for a in A:
    L[a] += 1
ans = 0
for i in range(int(100000.0) + 1):
    S = sum(L[i:i + 3])
    if ans < S:
        ans = S
print(ans)
