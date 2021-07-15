def s(n):
    return len(str(n))

def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    [w,m,k]=get()
    ans=0
    while w>= (10**s(m)-m)*s(m)*k:
        w-=(10**s(m)-m)*s(m)*k
        ans+=(10**s(m)-m)
        m=10**s(m)
    w=w//(k*(s(m)))
    ans+=(w)
    print(ans)
    
    if mode=="file":f.close()

def __starting_point():
    main()

__starting_point()
