import collections

n = int(input())

ss = [input() for i in range(n)]
c = collections.Counter(ss)
print(len(c))
