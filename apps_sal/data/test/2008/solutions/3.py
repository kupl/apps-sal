n=int(input())
que=[]
for i in range(n):
    a,b=[int(x) for x in input().split()]
    que.append((a-b,a,b))
que.sort(reverse=True)
counter=0
for i in range(n):
    counter+=que[i][1]*i+que[i][2]*(n-i-1)
print(counter)
    
    

