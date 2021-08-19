from itertools import accumulate
(N, K) = map(int, input().split())
mod = 10 ** 9 + 7
sqrt = int(N ** (1 / 2))
count = [N // i - N // (i + 1) for i in range(1, N // sqrt)] + [1] * sqrt
ansList = count
for _ in range(K):
    ansList = [i * j % mod for (i, j) in zip(accumulate(reversed(ansList)), count)]
print(ansList[-1])
