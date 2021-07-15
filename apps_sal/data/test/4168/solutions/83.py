n=int(input());result=[]
while n!=0:
  r=n%2
  n=(n-r)//-2
  result.append(r)
print(''.join(map(str,result[::-1])) if result else 0)
