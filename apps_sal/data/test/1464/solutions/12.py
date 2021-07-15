def ts(d,l):
    for i in range( len(l)):
        if d in l[i] :
            return(True)  
    return(False)
def main():
    n=int(input())
    l=[]
    d=''
    f=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(n):
        l.append(input())
    for j in range(20):
        for k in range (len(f)):
            for i in range(len(f)):
                d+=f[i]
                if ts(d,l):
                    d=d[:-1]
                else :
                    return(d)
            d=d[:-1]
            d+=f[k]
        
print(main())


