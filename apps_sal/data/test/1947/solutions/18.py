def inint():
    return int(input())
def inlist():
    return list(map(int,input().split()))

def main():
    n,m,l=inlist()
    aa=inlist()
    chg=0;ch=0
    a=[[i,0] for i in aa]
    for i in range(n):
        if aa[i]>l :
            if ch==0:
                ch+=1
                chg+=1
                a[i][1]=chg
            else:
                ch+=1
                a[i][1]=chg
        else:
            if ch!=0:ch=0
    sol=list()
    if n>1:
        for z in range(m):
            qu=input()
            if qu=="0":sol.append(chg)
            else:
                #print(chg)
                zz,p,d=list(map(int,qu.split()))
                p-=1
                a[p][0]+=d
                if a[p][1]==0 and a[p][0]>l:
                    if p>0 and p<n-1:
                        #print('first')
                        if a[p-1][1]==0 and a[p+1][1]==0:
                            chg+=1
                            a[p][1]=chg
                        elif a[p-1][1]==0 and a[p+1][1]>0:
                            a[p][1]=a[p+1][1]
                        elif a[p-1][1]>0 and a[p+1][1]==0:
                            a[p][1]=a[p-1][1]
                        else:
                            a[p][1]=a[p-1][1];chg-=1
                    elif p==0:
                        #print('second')
                        if a[p+1][1]==0:
                            chg+=1
                            a[p][1]=chg
                        else:
                            a[p][1]=a[p+1][1]
                    elif p==n-1:
                        #print('third')
                        if a[p-1][1]==0:
                            chg+=1
                            a[p][1]=chg
                        else:
                            a[p][1]=a[p-1][1]
    else:
        for z in range(m):
            qu=input()
            if qu=="0":sol.append(chg)
            else:
                #print(chg)
                zz,p,d=list(map(int,qu.split()))
                p-=1
                a[p][0]+=d
                if a[p][0]>d:chg=1
    #print(a,chg)
    print(*sol,sep='\n')





def __starting_point():
    #import profile
    #profile.run("main()")
    main()
__starting_point()
