def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")

    if mode=="file":n=int(f.readline())
    else:n=int(input())
    w=[]
    for i in range(2,2*n+1):
        if mode=="file":g=[int(x) for x in f.readline().split()]
        else:g=[int(x) for x in input().split()]
        for j in range(1,i):
            w.append([g[j-1],[i,j]])
    w.sort()
    free=2*n
    fr=[-1]*(free+1)
    w.reverse()
    for e,k in w:
        if fr[k[0]]==-1 and fr[k[1]]==-1:
            fr[k[0]]=k[1]
            fr[k[1]]=k[0]
            free-=1
            if free==0:
                break
    for i in fr[1:]:
        print(i,end=' ')
            

    if mode=="file":f.close()


def __starting_point():
    main()

__starting_point()
