import itertools
(n, m) = map(int, input().split())
li = [list(map(int, input().split())) for i in range(m)]
lis = list(itertools.chain.from_iterable(li))
for i in range(1, n + 1):
    print(lis.count(i))
