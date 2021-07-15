def main():
    N=int(input())
    pos={}
    P=list(map(int,input().split()))
    for i in range(N):
        pos[P[i]]=i
    end=N
    steps=[]
    while(end>1):
        if(pos[end]<(end-1)):
            start=pos[end]
            for j in range(start,end-1):
                pos[P[j]]=j+1
                pos[P[j+1]]=j
                
                temp=P[j]
                P[j]=P[j+1]
                P[j+1]=temp

                steps.append(j+1)
            end=start+1
        elif(pos[end]>(end-1)):
            break
        else:
            end-=1
    flag=True
    for i in range(N):
        if(P[i]!=(i+1)):
            flag=False
            break
    if(flag):
        if(len(steps)!=(N-1)):
            print((-1))
        else:
            for i in range(len(steps)):
                print((steps[i]))
    else:
        print((-1))
def __starting_point():
    main()

                
                

__starting_point()
