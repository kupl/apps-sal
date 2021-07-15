n=int(input())
j=0
l=0
for i in range(n):
    L=int(input())
    l+=int(i>0)+abs(L-j)+1
    j=L
print(l)
        

