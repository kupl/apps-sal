#解説方針
import math
N = int(input())
A = list(map(int, input().split()))

all_xor = 0
for i in range(N):
  all_xor = all_xor ^ A[i]

fore = A[0] ^ A[1]#S
back = fore ^ all_xor #X
#a + b = (a xor b) + 2 * (a and b)
#a xor b = back, a + b = A[0] + A[1]

a_and_b = (A[0] + A[1] - back) / 2
#print(a_and_b, back)
#a_and_bは非負整数である必要がある
if (a_and_b % 1 != 0) or (a_and_b < 0):
  print((-1))
  return
a_and_b = int(a_and_b)

#print(a_and_b, back, a_and_b & back)
#a_and_bとbackには共通のbitがない
if (a_and_b & back) != 0:
  print((-1))
  return

ans = a_and_b
#print(math.log2(32))
if back == 0:
  if (ans == 0):
    print((-1))
  else:
    print((A[0] - ans))
  return
else:
  if ans > A[0]:
    print((-1))
    return
  nn = int(math.log2(back)) + 1
  #print(nn)
  #print(2 >> 1)
  #print(2 << 1)
  for i in range(nn + 1):
    #print(back, nn - i)
    if ((back >> (nn - i)) & 1):
      #print(ans, 2 << (nn - i))
      k = ans + (1 << (nn - i))
      #print("k", k, i)
      if k <= A[0]:
        ans = k 
  if (ans == 0):
    print((-1))
  else:
    print((A[0] - ans))
  

