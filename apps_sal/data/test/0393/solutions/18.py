n=int(input())
ns=input()

def fun():
    if n==1:
        if ns[0]=='1':
            return 'Yes'
        else:
            return 'No'
    for i  in range(1,n):
        if ns[i]=='1' and ns[i-1]=='1':
            return('No')
    if n>=2:
        if ns[0] == '0' and ns[1] == '0':
            return 'No'
        if ns[-1] == '0' and ns[-2] == '0':
            return 'No'
    num=0
    for c in ns:
        if c=='0':
            num+=1
        if c=='1':
            num=0
        if num>2:
            return('No')
    if num>2:
        return 'No'
    return 'Yes'
print(fun())
