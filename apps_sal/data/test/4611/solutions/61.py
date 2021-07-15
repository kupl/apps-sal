n=int(input())
 
num,a,b=0,0,0
 
for i in range(n):
  t,x,y=map(int,input().split())
  num,a,b=abs(t-num),abs(x-a),abs(y-b)
  su=a+b
  if num>=su and num%2 == su%2:
    ans="Yes"
  else:
    ans="No"
    break
      
print(ans)
