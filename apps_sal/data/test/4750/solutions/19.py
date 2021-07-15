t=int(input())
for j in range(t):
    s=input()
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=int(s[i])
    result=''
    a=s[0]
    b=s[2]
    if b==a:
        b=b+1
    result=result+str(a)+' '+str(b)
    print(result)


