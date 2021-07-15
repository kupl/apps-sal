N,A,B = map(int,input().split())

sum = 0
#print (N//(A+B))


sum+=A*(N//(A+B))

if N%(A+B)>A:
  sum+= A
else :
  sum+= N%(A+B)
print (sum)
