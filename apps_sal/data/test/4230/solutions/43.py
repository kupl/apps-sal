X,N = list(map(int,input().split()))

p = list(map(int,input().split()))

count = 0

flg = False

lis=[]

result=0

while True:
    
    up = X+count
    
    down = X-count
    
    if p.count(down) ==0:
        lis.append(down)
        flg = True
    
    if p.count(up)==0:
        lis.append(up)
        flg = True
        
    
    if flg ==True:
        break
    else:
        count+=1
        

lis.sort()

print((lis[0]))

