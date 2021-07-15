N=int(input())
T=input()
S=T.replace("110","")
M=(len(T)-len(S))//3
INF=10**10
if N==1:
    if T=="1":
        print((2*INF))
    else:
        print(INF)
    return
if N==2:
    if T=="11":
        print(INF)
    elif T=="00":
        print((0))
    elif T=="10":
        print(INF)
    else:
        print((INF-1))
    return

suffix=["","0","10","110"]
prefix=["110","11","1",""]
for x in suffix:
    for y in prefix:
        if T==(x+"110"*M+y):
            if x=="" and y=="":
                print((INF-M+1))
            elif x!="" and y=="":
                print((INF-M))
            elif x=="" and y!="":
                print((INF-M))
            else:
                print((INF-M-1))
            return
print((0))

