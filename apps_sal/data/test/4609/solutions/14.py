import collections
n = int(input())
a = [int(input()) for i in range(n)]
print(sum([i % 2 == 1 for i in collections.Counter(a).values()]))
