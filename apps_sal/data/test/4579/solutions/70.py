import collections
N = int(input())
a = [input() for i in range(N)]
c = collections.Counter(a)
print(len(c))
