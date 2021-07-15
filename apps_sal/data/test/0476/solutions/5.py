def main():
    x=str(input())
    xix=int(x)
    xs=list(set(list(x)));
    if len(xs)==1 and xs[0]=='1':
        print ("YES")
    elif x[0]=="4":
        print ("NO")
    elif len(xs)==2:
        xs.sort()
        ncs="".join(xs)
        if ncs=="14":
            if len(x)>=3 and x[0:3]=="441":
                print ("NO")
            else:
                ind1=x.find("444")
                if ind1>=0 or x=="414":
                    print ("NO")
                else:
                    print ("YES")
        else:
            print ("NO")
    else:
        print ("NO")
    
main()
