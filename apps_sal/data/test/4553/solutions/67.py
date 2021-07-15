a,b=list(map(int,input().split()))
s=input()
if len(s) != a+b+1:
    print('No')
    return
else:
    if s[a] != '-':
        print('No')
        return
    elif s.count('-')!=1:
        print('No')
        return
print('Yes')
        

