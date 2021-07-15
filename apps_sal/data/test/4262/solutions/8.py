import itertools
n = int(input())
N = list(i for i in range(1,n+1))
L = itertools.permutations(N,n)
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
cnt, s, e = 0, 0, 0

for l in L:
  cnt += 1
  if a == l:
    s = cnt
  if b == l:
    e = cnt
print((abs(s-e)))


