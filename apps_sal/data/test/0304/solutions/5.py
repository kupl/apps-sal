n=int(input())
t=[]
a=[]
for i in range(10):
    t.append(0)
    a.append(1)
while n:
    a[n%10]+=1
    n//=10
ans=0
for i in range(a[0]!=1,a[0]):
    t[0]=i
    for i in range(a[1]!=1,a[1]):
        t[1]=i
        for i in range(a[2]!=1,a[2]):
            t[2]=i
            for i in range(a[3]!=1,a[3]):
                t[3]=i
                for i in range(a[4]!=1,a[4]):
                    t[4]=i
                    for i in range(a[5]!=1,a[5]):
                        t[5]=i
                        for i in range(a[6]!=1,a[6]):
                            t[6]=i
                            for i in range(a[7]!=1,a[7]):
                                t[7]=i
                                for i in range(a[8]!=1,a[8]):
                                    t[8]=i
                                    for i in range(a[9]!=1,a[9]):
                                        t[9]=i
                                        s=0
                                        for i in range(10):
                                            s+=t[i]
                                        w=1
                                        cnt=s
                                        for i in range(10):
                                            for j in range(t[i]):
                                                if i==0:w*=cnt-1
                                                else:w*=cnt
                                                cnt-=1
                                        for i in range(10):
                                            for j in range(1,t[i]+1):
                                                w//=j
                                        #print(w)
                                        ans+=w
print(ans)

