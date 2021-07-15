def main():
    mode="filee"
    if mode=="file":p=open("test.txt","r")
    #f.readline()
    #input()
    get = lambda :[int(x) for x in (p.readline() if mode=="file" else input()).split()]
    [a,b,c,d,e,f]=get()
    g=[[a,b,"A"],[c,d,"B"],[e,f,"C"]]
    n=0
    for i in g:n=max(n,max(i[:2]))
    if a*b + c*d + e*f !=n*n:
        print("-1")
        return
    h=[]
    print(n)
    for i in g:
        if n in i:
            for j in range(min(i[:2])):
                print(i[2]*max(i[:2]))
        else:
            h.append(i)
    if len(h)>0:
        for j in range(2):
            for k in range(2):
                if h[0][j]==h[1][k] and (h[0][1-j] + h[1][1-k])==n:
                    l1 = h[0][1-j]
                    l2 = h[1][1-k]
                    times = h[0][j]
                    c1 = h[0][2]
                    c2 = h[1][2]
                    break
        for i in range(times):
            print(c1*l1 + c2*l2)

    if mode=="file":p.close()


def __starting_point():
    main()

__starting_point()
