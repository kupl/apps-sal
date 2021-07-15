from itertools import *
 
N = input()
P = tuple(input().split(" "))
Q = tuple(input().split(" "))

a = 0
b = 0
c = 0
for p in permutations([str(i) for i in range(1, int(N)+1)]):
  if p==P:
    a = c
  if p==Q:
    b = c
  c += 1
print(abs(a-b))
