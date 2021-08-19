import itertools
(N, M) = list(map(int, input().split()))
res = []
for i in range(M):
    ab = list(map(int, input().split()))
    res.append(ab)
res = list(itertools.chain.from_iterable(res))
for i in range(N):
    print(res.count(i + 1))
