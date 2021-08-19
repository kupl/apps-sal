from collections import defaultdict
(N, *A) = map(int, open(0).read().split())
dic1 = defaultdict(lambda: -10 ** 20)
dic2 = defaultdict(lambda: -10 ** 20)
for i in range(-1, N):
    dic1[i, 0] = 0
    dic2[i, 0] = 0
for i in range(N):
    for j in range(max(1, N // 2 - (N - i + 1) // 2), i // 2 + 2):
        dic1[i, j] = max(dic1[i, j], dic2[i - 1, j - 1] + A[i])
    for j in range(N // 2 - (N - i) // 2, (i - 1) // 2 + 2):
        dic2[i, j] = max(dic2[i - 1, j], dic1[i - 1, j])
print(max(dic1[N - 1, N // 2], dic2[N - 1, N // 2]))
