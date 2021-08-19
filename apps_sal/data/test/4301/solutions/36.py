import collections
n = int(input())
a = [int(input()) for i in range(n)]
m = sorted(list(set(a)))
c = collections.Counter(a)
t = [max(a)] * n
if c[max(a)] == 1:
    t[a.index(max(a))] = m[-2]
[print(i) for i in t]
