s1=input()
s2=input()
dp=[0 for i in range(len(s1))]
if (s1[0]==s2[0]) and (s1[0]=='0'):
    r=2
elif (s1[0]==s2[0]) and (s1[0]=='X'):
    r=0
else:
    r=1
for i in range(1,len(s1)):
    if (s1[i]==s2[i]) and (s1[i]=='X'):
        dp[i]=dp[i-1]
        r=0
    elif (s1[i]!=s2[i]) and (r<=1):
        dp[i]=dp[i-1]
        r=1
    elif ((s1[i]==s2[i]) and (s1[i]=='0')):
        if r==2:
            dp[i]=dp[i-1]+1
            r=1
        elif r==1:
            dp[i]=dp[i-1]+1
            r=0
        else:
            dp[i]=dp[i-1]
            r=2
    else:
        dp[i]=dp[i-1]+1
        r=0
print(dp[len(s1)-1])
        
        


