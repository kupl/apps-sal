'''
分かりやすい図解ページ
https://blog.bobuhiro11.net/2019/08-03-abc135ef.html
https://betrue12.hateblo.jp/entry/2019/07/28/215024
'''
import math

def swap(X,Y):
  temp=X
  X=Y
  Y=temp
  return X,Y

def keiro(count,X,Y,K):
  keirolist=[]
  oneway_surplus=int(((count*K)-X-Y)/2)
  move=0
  turncount=0
  prevX=0
  prevY=0
  while(move<count):
    if turncount==0:
      if K-prevY>=oneway_surplus:
        prevX=K-oneway_surplus
        prevY-=oneway_surplus
        turncount+=1
      else:
        prevX=0
        prevY-=K
    elif turncount==1:
      if K+prevX>X:
        prevY+=(K-(X-prevX))
        prevX=X
        turncount+=1
      else:
        prevX+=K
    else:
      prevY+=K
    keirolist.append([prevX,prevY])
    #print(keirolist)
    move+=1
  return keirolist

def ans(K,X,Y):
  anslist=[]
  count=0
  Xminus=0
  Yminus=0
  swapflag=0
  if X<0:
    Xminus=1
    X=abs(X)
  if Y<0:
    Yminus=1
    Y=abs(Y)
  if (X+Y)==K:
    count=1
    anslist.append([X,Y])
  else:
    if X<Y:
      X,Y=swap(X,Y)
      swapflag=1
    if X+Y>K:
      count=math.ceil((X+Y)/K)
      lastflag=0
      if (count*K-X-Y)%2==1:
        count+=1
        lastflag=1
      anslist=keiro(count,X,Y,K)
      
    else:
      if (X+Y)%2==0:
        count=2
        anslist=keiro(count,X,Y,K)
      else:
        count=3
        anslist.append([X,-K+X])
        Xsurplus=int((X+K-Y)/2)
        anslist.append([X+Xsurplus,X-Xsurplus])
        anslist.append([X,Y])
  for ans in anslist:
    if swapflag==1:
      ans[0],ans[1]=swap(ans[0],ans[1])
    if Xminus==1:
      ans[0]=-ans[0]
    if Yminus==1:
      ans[1]=-ans[1]
  return count,anslist



K=int(input())
X,Y=map(int,input().split())

if K%2==0 and (X+Y)%2==1:
  print(-1)
  return

count,anslist=ans(K,X,Y)
print(count)
for ans in anslist:
  print(ans[0],ans[1])
