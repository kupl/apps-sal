x = input()
l=len(x)
a=int(input())
b=list(map(int,input().split(' ')))
b.sort()
sumx=[0]*len(x)+[0]
pt = 0
for i in range(1, l//2+1):
    t=0
    if pt<len(b):
        while b[pt] == i:
            pt += 1
            
            t+=1
            if not pt < len(b):
                break
    sumx[i] = sumx[i-1]+t
sumx = sumx[1:]
tt = sumx[:len(sumx)//2]
tt.reverse()
if l%2==1:
    sumx = sumx[:len(sumx)//2]+[0]+tt
else:
    sumx = sumx[:len(sumx)//2]+tt
strx=''
for i in range(l):
    if sumx[i]%2==1:
        strx+=x[l-1-i]
    else:
        strx += x[i]
print(strx)
