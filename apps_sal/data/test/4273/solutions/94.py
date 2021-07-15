from itertools import combinations as cmbs
c = {"M":0,"A":0,"R":0,"C":0,"H":0}
for i in range(int(input())):
  si = input()
  if si[0] in c:
    c[si[0]] += 1
ans = 0
for i,j,k in cmbs(c.values(),r=3):
  t = i*j*k
  ans += t
print(ans)
