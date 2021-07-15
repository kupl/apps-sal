from heapq import heappop,heappush
n,k=map(int,input().split())
s=[]
h=set()#種類
l=[0]*n #個数について
for _ in range(n):
    t,d=map(int,input().split())
    s.append((d,t-1))
s=sorted(s,reverse=True)
a=[]#heapq
num=0#美味しさのわ
for i in range(k):
    d,t=s[i]
    l[t]+=1
    h.add(t)
    num+=d
    if l[t]>1:
        heappush(a,(d,t))#２種類以上ならheapqにたす
ans=len(h)**2+num
for j in range(k,n):
    d,t=s[j]#次に小さいのを引いてくる
    l[t]+=1
    if  l[t]>=2:
        continue #2以上ならむし
    if len(a)==0:
        break
    d1,t1=heappop(a) #いらないのを引く
    h.add(t)
    num=num-d1+d
    ans=max(ans,len(h)**2+num)
print(ans)
