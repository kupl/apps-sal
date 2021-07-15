from collections import defaultdict
    
n=int(input())
C=[]
cnt=0
D=defaultdict(int)

for i in range(n) :
    C.append([int(i) for i in input().split()])

for i0 in range(n) :
    x0=C[i0][0]
    y0=C[i0][1]
    for Dots in C[i0+1:] :
        x=Dots[0]-x0
        y=Dots[1]-y0
        if x<0 :
            x,y=-x,-y
        elif x==0 :
            if y<0 :
                y=-y
        cnt+=D[(x,y)]
        D[(x,y)]+=1

print(int(cnt/2))
