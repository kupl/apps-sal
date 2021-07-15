n,m=map(int,input().split())                       
h =list(map(int,input().split()))
cnt = 0
l = [[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split()) 
    l[a-1].append(h[b-1])
    l[b-1].append(h[a-1])

for i in range(n):
    if l[i] == []:
        cnt+=1

    elif h[i] > max(l[i]):
        cnt +=1
    

print(cnt)
