t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    count0=0
    count1=0
    for i in range(n):
        if s[i]=='0':
            count0+=1
        else:
            count1+=1
    if min(count0,count1)%2==0:
        print('NET')
    else:
        print('DA')
