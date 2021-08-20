import collections
(N, *A) = map(int, open(0).read().split())
c = collections.Counter(A)
print(sum([1 for x in c.values() if x % 2 == 1]))
