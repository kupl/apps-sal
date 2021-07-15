t=int(input())
for i in range(1,t+1):
   
    a=[]
    s=input()
    j=0
    while j<=len(s)-1:
        if (s[j]=='o'):
            u=True
            if j>=2:
                if ((s[j-2]=='t') and (s[j-1]=='w')):
                    if j<=len(s)-2:
                        if s[j+1]=='o':
                            a.append(j)
                        else:
                            a.append(j+1)
                            u=False
                    else:
                        a.append(j)
                    
                    
            if j<=len(s)-3:
                if ((s[j+2]=='e') and (s[j+1]=='n')):
                    if u:
                        a.append(j+2)
                    j+=3
                else:
                    j+=1
            else:
                j+=1
        else:
            j+=1
                
    print(len(a))
    if len(a)!=0:
        print(*a)
    else:
        print()
        
                

