def main():
    n,m=list(map(int,input().split()))
    s=input()
    
    route=[]
    i=n
    visited=n
    while True:
        if i-m<=0:
            route.append(i)
            break
        else:
            flag=False
            for j in range(i-m,visited):
                if flag:
                    break
                if s[j]=='0':
                    route.append(i-j)
                    visited=i-m
                    i=j
                    flag=True
            if flag:
                continue
            else:
                print((-1))
                return
    
    print((*route[::-1]))
def __starting_point():
    main()


__starting_point()
