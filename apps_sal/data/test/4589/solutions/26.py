h,w=map(int,input().split())
a=[input() for i in range(h)]
b=[]
c=0
for i in range(h):
    for j in range(w):
        if a[i][j]=='#':
                b.append("#")
        else:
            for k in a[max(0,i-1):min(h,i+2)]:
                c+=k[max(0,j-1):min(w,j+2)].count("#")
            b.append(str(c))
            c=0
            
d="".join(b)
for i in range(h):
    print(d[i*w:(i+1)*w])
