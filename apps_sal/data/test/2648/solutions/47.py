import collections
n = int(input())
a = list(map(int, input().split()))
kind = collections.Counter(a)
if len(kind) % 2 == 0:
    print(len(kind) - 1)
else:
    print(len(kind))
