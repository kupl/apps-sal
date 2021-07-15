import itertools
n = int(input())
p = "".join(input().split())
q = "".join(input().split())
l = list(range(1,n+1))
i = 0
for v in itertools.permutations(l, n):
  i += 1
  j = "".join(map(str, v))
  if p == j:
    a = i
  if q == j:
    b = i
print(abs(a-b))
