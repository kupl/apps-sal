N,A,B,C = map(int,input().split())

L = [int(input()) for i in range(N)]

# L本の竹を、A,B,C,0(使わない)に振り分ける全探索 4^N = 約60000通り

ans = 10 ** 10
import itertools
for prod in itertools.product(range(4), repeat = N):
  bamboo = [0] * 4
  mp = 0
  for i in range(len(prod)):
    if prod[i] == 0:
      continue
    if bamboo[prod[i]] != 0:
      mp += 10
    bamboo[prod[i]] += L[i]
  if 0 in bamboo[1:]:
    continue
  mp += abs(A - bamboo[1]) + abs(B - bamboo[2]) + abs(C - bamboo[3])
  if ans > mp:
    ans = mp
    
print(ans)
