n,m=map(int,input().split())
if (n*m<4 and (n==1 or m==1)) or (n*m<5 and (n!=1 and m!=1)):
    print(0)
else:
    l=n*m
    if n%2==0 and m%2==0:
        if n==m:
            if n%3!=0 and n%4!=0:
                print(l-4)
            else:
                print(l)
        else:
            if n%4==0 or m%4==0:
                print(l)
            elif n%3==0 or m%3==0:
                print(l)
            else:
                print(l-2)
    elif n%2!=0 and m%2!=0:
        if n==1 or m==1:
            z=max(n,m)
            if z%6==0:
                print(z)
            else:
                s1=(z//6)*6
                r=z%6
                if r>3:
                    s1=s1+2
                    r=r%4
                    s1=s1+(r*2)
                print(s1)
        else:
            print(l-1)
    #case3
    else:
        if n==1 or m==1:
            z=max(n,m)
            if z%6==0:
                print(z)
            else:
                s1=(z//6)*6
                r=z%6
                if r>3:
                    s1=s1+2
                    r=r%4
                    s1=s1+(r*2)
                print(s1)
        else:
            if n%4==0 or m%4==0:
                print(l)
            elif n%6==0 or m%6==0:
                print(l)
            else:    
                if n%2==0:
                    z=m
                else:
                    z=n
                if z%4==1:
                    print(l)
                else:
                    if z>=6:
                        if z%6==1:
                            if z>7 and z%4==3:
                                print(l)
                            else:
                                print(l-2)
                        elif z%6==5 and z%4==3:
                            print(l)    
                        elif z%6==3:
                            print(l)
                    else:
                        print(l-2)
