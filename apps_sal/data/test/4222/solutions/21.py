import itertools
(N, K) = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    array = list(map(int, input().strip().split()))
    A.append(array)
X = list(itertools.chain.from_iterable(A))
X = list(set(X))
print(N - len(X))
