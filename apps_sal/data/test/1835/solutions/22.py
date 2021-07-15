for i in range(int(input())):
    n=int(input())
    cnt0,cnt1,cnt2=0,0,0
    for i in range(n):
        x=input()
        cnt2+=len(x)&1
        for i in x:
            if i=='0':
                cnt0+=1
            else:
                cnt1+=1
   # print(cnt0,cnt1,cnt2)
    if((cnt2-(cnt0&1)-(cnt1&1))%2==1) or (cnt0&1 and cnt1&1 and cnt2==0):
        print(n-1)
    else:
        print(n)
