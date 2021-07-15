N = int(input())

L = list(map(int, input().split()))
L_sort = sorted(L)
Y_count = 0
N_count = 0

import itertools
for x in itertools.combinations(L_sort, 3):
  if x[0] != x[1] and x[1] != x[2] and x[0]!= x[2] and x[0]+ x[1] >+ x[2] and x[1]+x[2] >= x[0] and x[0]+x[2] >= x[1]:
    Y_count = Y_count +1
  else:
    N_count = N_count +1

print(Y_count)
