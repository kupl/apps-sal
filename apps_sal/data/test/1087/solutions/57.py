import math
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
D = len(bin(max(A))) - 2
O = max(len(bin(K)) - 2, D)
M = N / 2
L = [0] * D
C = [1] * O
for a in A:
    s = str(bin(a))[2:]
    l = list(s.zfill(D))
    L = [int(i) + j for (i, j) in zip(l, L)]
L = (O - D) * [0] + L
x = 0
for i in range(O):
    tmp = 0
    if L[i] < M:
        tmp = 2 ** abs(O - i - 1)
        if x + tmp <= K:
            x += tmp
ans = 0
for a in A:
    ans += x ^ a
print(ans)
