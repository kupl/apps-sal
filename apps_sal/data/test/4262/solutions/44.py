import itertools
n = int(input())
s = ""
for i in range(n):
    s += str(i + 1)
l = list(itertools.permutations(s, n))
p = tuple(input().split())
q = tuple(input().split())
a = l.index(p)
b = l.index(q)
print(abs(a - b))
