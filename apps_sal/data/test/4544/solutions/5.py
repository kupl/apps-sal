import collections

n = int(input())
a = list(map(int, input().split()))
b = list(map(lambda x: x - 1, a))
c = list(map(lambda y: y + 1, a))
d = a + b + c

e = collections.Counter(d)
print(max(e.values()))
