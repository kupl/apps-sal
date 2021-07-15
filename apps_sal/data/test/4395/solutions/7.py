n=int(input())
s=input()
lens=len(s)
ans,ans2=10**9,""

for ca in range(6):
    if 0<=ca<=1:
        st="R"
    elif 2<=ca<=3:
        st="G"
    else:
        st="B"

    ss=[0]*lens
    for i in range(lens):
        ss[i]=st
        if st=="R":
            if ca%2==0: st="G"
            else: st="B"
        elif st=="G":
            if ca%2==0: st="B"
            else: st="R"
        else:
            if ca%2==0: st="R"
            else: st="G"

    diff=0
    for i in range(lens):
        if ss[i]!=s[i]: diff+=1

    if diff<ans:
        ans,ans2=diff,"".join(ss)

print(ans,ans2,sep="\n")
