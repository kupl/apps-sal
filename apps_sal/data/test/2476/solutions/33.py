from itertools import accumulate
(N, *A) = map(int, open(0).read().split())
C = [0] * (N + 1)
D = [0] * (N + 1)
for a in A:
    C[a] += 1
    D[C[a]] += 1
T = [0] + [s // i for (i, s) in enumerate(accumulate(D[1:]), 1)]
ans = []
x = N
for k in range(1, N + 1):
    while 0 < x and T[x] < k:
        x -= 1
    ans.append(x)
print('\n'.join(map(str, ans)))
