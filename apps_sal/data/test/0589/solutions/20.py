def main():
    s=input()
    l=[]
    i=1
    result=1
    
    for i in range(len(s)):
        if s[i:i+1]=='?':
            if i==0:
                result=result*9
            else:
                result=result*10
        if s[i:i+1]>='A' and s[i:i+1]<='J':
            if i==0:
                result=result*9
                l.append(s[i:i+1])
                
            else:
                if l.count(s[i:i+1])==0:
                    result=result*(10-len(l))
                    l.append(s[i:i+1])
                    
     
    print(result)
                
def __starting_point():
    main()

__starting_point()
