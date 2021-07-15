import collections

n = int(input())
s = [''.join(sorted(list(input()))) for _ in range(n)]

c = collections.Counter(s)
print(sum([i*(i-1)//2 for i in c.values()]))
