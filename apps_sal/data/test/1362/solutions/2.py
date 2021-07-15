n,p,m=list(map(int,input().split()))
flag,t_neg,t_in,d,tot=0,0,0,1,0

for i in range (n):
    ini_d=d
    if flag==1:
        tot+=(t-p)
        if tot<0:
            t_neg+=1
    d,t=list(map(int,input().split()))
    if flag==0:
        t_neg=(d-ini_d)
        tot=t_neg*-p
        flag=1
    else:
        tot+=(((d-1)-ini_d)*-p)
        if tot<0:
            if tot<=(((d-1)-ini_d)*-p):
                t_neg+=(d-1)-ini_d
            else:
                x=int(-tot%p)
                y=int(-tot/p)
                if x!=0:
                    t_neg+=(y+1)
                else:
                    t_neg+=y



ini_d=d
tot+=(t-p)
if tot<0:
    t_neg+=1
tot+=(((m)-ini_d)*-p)
if tot<0:
    if tot<=(((m)-ini_d)*-p):
        t_neg+=(m)-ini_d
    else:
        x=int(-tot%p)
        y=int(-tot/p)
        if x!=0:
            t_neg+=(y+1)
        else:
            t_neg+=y

                    
print (t_neg) 
    

