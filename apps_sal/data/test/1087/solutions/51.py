import numpy as np
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 最大桁数調べる
MAX = max(len(bin(K)[2:]), len(bin(max(A))[2:]))


L = [[0] * MAX for _ in range(N)]
for i, a in enumerate(A):
    b = bin(a)[2:]
    b = b.zfill(MAX)
    for j, s in enumerate(b):
        if s == "1":
            L[i][j] += 1
L = np.array(L)
count = 0
ones = L.sum(axis=0)
# print(ones)
for i in range(MAX):
    if ones[i] * 2 == N:
        continue
    elif ones[i] * 2 < N:
        add = 2**(MAX - 1 - i)
        if count + add <= K:
            count += add
    else:
        continue

ans = 0
for a in A:
    ans += (count ^ a)
print(ans)
