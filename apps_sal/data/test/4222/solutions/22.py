import itertools

N, K = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))
A = list(itertools.chain.from_iterable(A))

count = 0
for i in range(1, N + 1):
    if not i in A:
        count += 1
print(count)
