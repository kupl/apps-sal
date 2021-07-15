# cook your dish here
n=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
t=list(map(lambda x, y:(x,y), s, f)) 
#ts=sorted(t,key=lambda x:x[0])
#print(ts)
end=0
tt=[]
k=0
for i,j in t:
     if(not (tt)):
          tt.append(k)
          end=j
          k+=1
          continue
     if(i>=end):
          tt.append(k)
          end=j
     k+=1
for i in tt:
     print(i,end=" ")
print()
     
