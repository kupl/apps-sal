def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    m=get()
    w=get()
    h=get()
    ans=0
    s=500
    for i in range(5):
        ans+=max(0.3*s, (1- m[i]/250)*s - 50*w[i])
        s+=500
    ans+=(100*h[0] - 50*h[1])
    print(int(ans))
    


    if mode=="file":f.close()


def __starting_point():
    main()

__starting_point()
