S=input()
cnt=0
if S[0]=='R':
    cnt+=1
    if S[1]=='R':
        cnt+=1
        if S[2]=='R':
            cnt+=1
        else:
            pass
else:
    if S[1]=='R':
        cnt+=1
        if S[2]=='R':
            cnt+=1
        else:
            pass
    else:
        if S[2]=='R':
            cnt+=1

print(cnt)
