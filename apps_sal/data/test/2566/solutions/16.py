t=int(input())
for i in range(t):
    k=int(input())
    week=[int(x) for x in input().split()]
    i=1
    need={}
    happy=sun=0
    answer=10**100
    for item in week:
        if item==1:
            happy+=1
            need[happy]=i
        i+=1
    week.reverse()
    for item in week:
        if item==0:
            sun+=1
        else:
            break
    week.reverse()
    need[0]=0
    i=happy
    for item in week:
        if item==1:
            counter=8-need[happy-i+1]+((k-i)//happy)*7+need[(k-i)%happy]
            if (k-i)%happy==0:
                counter-=sun
            answer=min(answer,counter)
            i-=1
    print(answer)
            
            

