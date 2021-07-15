n = int(input())
s = input()
ans = len(s)
i = 0
while (i<len(s)-1):
    if (s[i]=='U') and (s[i+1]=='R'):
        ans = ans-1
        i+=1
    elif (s[i]=='R') and (s[i+1]=='U'):
        ans-=1
        i+=1
    i+=1    
print(ans)        
    
        
    

    

