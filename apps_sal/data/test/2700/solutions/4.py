t=eval(input())
results=[]
for a0 in range(t):
 a,b,c,d=[float(x) for x in input().split()]
 flag=[a,b]
 flag.sort()
 a,b=flag[0],flag[1]
 flag=[c,d]
 flag.sort()
 c,d=flag[0],flag[1]
 if c<a and d<a:
  results.append(0)
  continue
 if c>b:
  results.append(int((b-a+1)*(d-c+1)))
  continue
 if c==b:
  results.append(int((b-a+1)*(d-c+1)-1))
  continue
 if c<b and d>b and c>a:
  s=((c-a)*(d-c+1))+(((b-c+1)/2)*((d-b)+(d-c)))
  results.append(int(s))
  continue
 if c<b and d>b and c<a:
  c=a+1
  s=((c-a)*(d-c+1))+(((b-c+1)/2)*((d-b)+(d-c)))
  results.append(int(s))
  continue
 if c<b and d<b and c>a:
  s=((c-a)*(d-c+1))+(((d-c)/2)*(d-c+1))
  results.append(int(s))
  continue
 if c<a and d<b:
  c=a+1
  s=((c-a)*(d-c+1))+(((d-c)/2)*(d-c+1))
  results.append(int(s))
  continue
for a1 in range(len(results)):
 print(results[a1])

