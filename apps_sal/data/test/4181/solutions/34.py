n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt=0
for i in range(n):
  c=b[i]-a[i]
  
  #city_iのみ攻撃
  if c<=0:
    cnt+=b[i]
  
  #city_i+1も攻撃
  else:
    d=b[i]-a[i+1]-a[i]
    
    #city_i+1生き残る
    if d<=0:
      cnt+=b[i]
      a[i+1]-=c
      
    #オーバキル
    else:
      cnt+=a[i]+a[i+1]
      a[i+1]=0
      
print(cnt)
