import sys
def main():
    
    l=sys.stdin.readline()

    l=sys.stdin.readline()
    l=l.split()
    for i in range(len(l)):
        l[i]=int(l[i])
    
    ser=len(l)-1
    dim=0
    s_ser=0
    s_dim=0
 
    while ser>dim:
        
        if l[dim] > l[ser]:
            s_ser+=l[dim]
            dim+=1
        else:
            s_ser+=l[ser]
            ser-=1
        if l[dim] > l[ser]:
            s_dim+=l[dim]
            dim+=1
        else:
            s_dim+=l[ser]
            ser-=1
       
    if ser==dim:
        s_ser+=l[ser]
    print (s_ser , s_dim)

def __starting_point():
    main()
__starting_point()
