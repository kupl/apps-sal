n,h=list(map(int,input().split()))
ip=list(map(int,input().split()))
width=0
for i in range(n):
    if ip[i]>h:
        width+=2
    else:
        width+=1
print(width)

