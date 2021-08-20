import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
ans = list(itertools.permutations(p))
ans.sort()
p = ans.index(p)
q = ans.index(q)
print(abs(p - q))
