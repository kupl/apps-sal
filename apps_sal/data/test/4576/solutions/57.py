s = [int(input()) for i in range(4)]
A = s[0]
B = s[1]
C = s[2]
X = s[3]
res = 0
total = 0
for a in range(A+1):
  for b in range(B+1):
    for c in range(C+1):
      total = 500*a + 100*b + 50*c
#      print("A:"+str(a)+" B:"+str(b)+" C:"+str(c) + "total:"+str(total))
      if(total == X):res = res +1
print(res)
