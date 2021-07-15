import sys
A, B = [int(x) for x in input().split()]
S = list(input())
for i in range(A+B+1):
  if(i==A):
    if(S[i]!='-'):
      print('No')
      return
  else:
    if(str.isdecimal(S[i])==False):
      print('No')
      return
print('Yes')
