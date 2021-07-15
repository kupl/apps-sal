import sys
r = lambda : list(map(int,input().split()))

n = int(input())
a = []
for i in range(n) :
    a.append(list(r()))
goods = list(range(n))
#print(goods)
for i in range(n) :
    for j in range(n) :
        if i==j or a[i][j]==0 or a[i][j]==-1 : continue 
        if a[i][j]==1 and i in goods : goods.remove(i);#print(i+1)
        if a[i][j]==2 and j in goods : goods.remove(j);#print(j+1)
        if a[i][j]==3 :
            if i in goods : goods.remove(i)
            if j in goods : goods.remove(j)

print(len(goods))
#print(goods)
print(' '.join([str(goods[i]+1) for i in range(len(goods))]))
    

