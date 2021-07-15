n = int(input())
def cal(a):
  cn = 0
  for i in range(1,a+1):
    if a%i==0: cn+=1
  return cn == 8
ans = 0
for i in range(1,n+1):
  if  (i%2==1) :ans += cal(i) 
print(ans)

