n,k=map(int,input().split())
a=[int(x) for x in input().split()]
mod=10**9+7
nega=sorted([a[i] for i in range(n) if a[i]<0],reverse=True)

ans=1
if k==n:
  # 全掛け算
  for i in a:
    ans*=i; ans%=mod
elif k%2 and n==len(nega):
  # 答えは負
  for i in range(k):
    ans*=nega[i]; ans%=mod
else:
  # 答えは正
  a=sorted(a, key=lambda x:abs(x), reverse=True)
  pi=ni=-1; cnt=0;
  x=[]
  for i in range(k):
    x.append(a[i])
    if a[i]<0: ni=i; cnt+=1
    if a[i]>0: pi=i;
  if cnt%2:
    t=a[k:]
    mx=max(t)
    mn=min(t)
    if mn>0 or pi==-1: # もう正しかとれる数値が存在していない
      x.append(mx)
      x.remove(a[ni])
    elif mx<=0: # もう負しかとれる数値が存在していない
      #if mx==0: print(0); return;
      x.append(mn)
      x.remove(a[pi])
    elif abs(a[pi]*mx)<=abs(a[ni]*mn):
      x.append(mn)
      x.remove(a[pi])
    else:
      x.append(mx)
      x.remove(a[ni])
  #print(x)
  for i in range(k):
    ans*=x[i]; ans%=mod;

print(ans)
