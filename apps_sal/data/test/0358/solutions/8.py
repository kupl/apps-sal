I = lambda : map(int,input().split())
visited = [False for i in range (10**6+1)]
#prime = {}
a , b , k  =I()
visited[1] = True
li = []
for i in range(2,int(b**(0.5))+1) :
    #print(visited[:14])
    if visited[i] == False :
        #prime[i] = 1
        for j in range (i+i,b+1 , i) :
            visited[j] =True
for i in range (a,b+1)   :
    if visited[i] == False :
        li.append(i)
ans = 0 
maxx = 0 
#print(li)
t1 = a
#print(li)
if len(li) < k :
    print("-1");return
n = len(li)
for i in range (n-k+1) :
    ans = li[i+k-1] -t1 + 1
    #print(ans)
    maxx = max(maxx,ans)
    t1 = li[i] + 1
ww = b - li[-k] + 1
#print(ww)
maxx = max(ww,maxx)
print(maxx)
