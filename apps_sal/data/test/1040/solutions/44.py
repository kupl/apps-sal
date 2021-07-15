N=int(input())
S=input()


ans=0
que =""

for s in S:
    if s in ["f","o"]:
        que = "".join([que,s])
    elif s=="x":
        if len(que)>=2 and que[-2:]=="fo":
            ans+=1
            que=que[:-2]
        else:
            que=""
    else:
        que=""
    #print(que)
print(N-3*ans)
