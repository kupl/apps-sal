S=input()
T=input()

lt=len(T)
ls=len(S)
S+='%'*lt

if ls<lt:
    flg=0
else:
    for i in range(ls-lt+1,-1,-1):
        # print('***',S[i:i+lt])
        flg=1
        for j in range(i,i+lt):
            s=S[j]
            # print(s,T[j-i])
            if s=='?': continue
            if s=='%' or s!=T[j-i]:
                flg=0
                break
        if flg==1:
            break
if flg:
    print((S[0:i]+T+S[i+lt:ls]).replace('?','a'))
else:
    print('UNRESTORABLE')
