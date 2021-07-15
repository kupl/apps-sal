def readinput():
    n,k=list(map(int,input().split()))
    s=input()
    return n,k,s

def main(n,k,s):
    nl=s.count('L')
    nr=n-nl
    if nl==0 or nr==0:
        return n-1
    
    c=['L','R']

    # happyの初期値を計算
    flip=[]
    happy=0
    if s[0]=='L':
        ci=0
    else:
        ci=1
    l=0
    for i in range(n):
        #print(s[i],c[ci])
        if s[i]==c[ci]:
            l+=1
            #print(l)
        else:
            #print(l)
            happy+=max(l-1,0)
            flip.append(ci)
            l=1
            ci=(ci+1)%2
    else:
        happy+=max(l-1,0)
    #print(flip,happy)
    return happy+min(2*k,len(flip))

def __starting_point():
    n,k,s=readinput()
    ans=main(n,k,s)
    print(ans)

__starting_point()
