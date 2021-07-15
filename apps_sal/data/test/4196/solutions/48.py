N=int(input())
*A,=map(int,input().split())

def gcd(a,b):
  if b==0:return a
  return gcd(b, a%b)

def cum(array, merge, unit):
    new=[unit]
    for i in range(len(array)):
        new.append(merge(new[-1], array[i]))
    return new
  
cum1 = cum(A,gcd,A[0])
cum2 = cum(A[::-1],gcd,A[-1])[::-1]

res=[]
for i in range(N):
  if i == 0:
    tmp = cum2[i+1]
  elif i == N-1:
    tmp = cum1[i]
  else:
    tmp = gcd(cum1[i],cum2[i+1])
  res.append(tmp)
  
print(max(res))
