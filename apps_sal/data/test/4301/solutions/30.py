n = int(input())
L = list(int(input()) for _ in range(n))
SL = sorted(L)
first_max = SL[-1]
second_max = SL[-2]
for l in L:
  if (l == first_max):
    print(second_max)
  else:
    print(first_max)
