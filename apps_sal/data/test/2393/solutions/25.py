t=int(input())
for i in range(t):
    s=input()
    ans=[]
    for i in range(1,len(s)-1):

        if s[i]=='w' and s[i-1]=='t' and s[i+1]=='o' and i+3<len(s) and s[i+2]=='n' and s[i+3]=='e':
            ans.append(i+1+1)
        elif s[i]=='n' and s[i-1]=='o' and s[i+1]=='e' and (len(ans)==0 or ans[len(ans)-1]!=i):
            ans.append(i+1)
        elif s[i]=='w' and s[i-1]=='t' and s[i+1]=='o':
            ans.append(i+1)
    print(len(set(ans)))
    print(*list(set(ans)))
