n=int(input())
a=list(map(int,input().split()))
h={}
for i in a:
    h[i-1]=0

tb=0
end=-1
for i in a:
    h[i]=h[i-1]+1
    if tb<h[i]:
        tb=h[i]
        end=i
arr=[]
start=end-tb+1
for i in range(n):
    if a[i]==start:
        arr.append(i+1)
        start+=1

print(tb)
print(*arr)

