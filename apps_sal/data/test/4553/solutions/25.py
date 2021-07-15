a,b=list(map(int,input().split()))
s=input()
if len(s) != a+b+1:
    print('No')
    return
else:
    if s[a] != '-':
        print('No')
        return
    else:
        for i in range(0,a):
            if s[i] == '-':
                print('No')
                return
        for i in range(a+1,a+b+1):
            if s[i] == '-':
                print('No')
                return
print('Yes')
        

