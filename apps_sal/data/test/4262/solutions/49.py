import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

l = [i + 1 for i in range(n)]

perm_li = [v for v in itertools.permutations(l)]

print((abs(perm_li.index(p) - perm_li.index(q))))
