import math
acc = []
n = int(input())
def OneNum (num, One):
 onetrans = num // acc[One]
 num = num % acc[One] 
 if num == 0:
  return onetrans*One
 else:
  return onetrans*One + min(OneNum(num, One-1), One + OneNum(acc[One] - num, One - 1))
acc.append(0)
for i in range(1,17):
 acc.append (acc[i-1]*10 + 1)
print (OneNum(n,16))
