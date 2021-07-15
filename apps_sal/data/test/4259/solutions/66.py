k=int(input())
a,b= map(int, input().split())
q=0

for i in range(1,1000):
  if a<=k*i and k*i<=b:
    print('OK')
    q=1
    break

if q==0:
  print('NG')
