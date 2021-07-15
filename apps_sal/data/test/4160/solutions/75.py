x=int(input())
m=100
cnt=0
while m<x:
    #m=int(m*1.01)
    m+=m//100
    cnt+=1
print(cnt)

