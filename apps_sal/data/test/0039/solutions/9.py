s = input()
isp = 1
onl = 1
for i in range(len(s)):
    if (i>0 and s[i-1]!=s[i]):
        onl = 0
    if (s[i]!=s[len(s)-i-1]):
        isp = 0
if (not isp):
    print(len(s))
else:
    if (onl):
        print(0)
    else:
        print(len(s)-1)
    


            
        
    
    
    
    
        
    
    
    

    
    
   


