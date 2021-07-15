import itertools
import sys

def score(abcd, A):
  ans = 0
  for a,b,c,d in abcd:
    if(A[b-1]-A[a-1])==c:
      ans += d
  return ans

N, M, Q = [int(x) for x in input().split()]
abcd = [ [int(x) for x in input().split()] for i in range(Q)]

a = itertools.combinations_with_replacement(range(1,M+1), N)
a = list(a)
Ans = 0
for i in range(len(a)):
  Ans = max(Ans,score(abcd,list(a[i])))
            
print(Ans)
