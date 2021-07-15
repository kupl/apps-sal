tx=int(input())
for i in range(tx):
    a,b=[int(i) for i in input().split()]
    k=a
    t=1
    t2=0
    s=str(a)
    for i in s:
        t2+=ord(i)-ord('0')
    while t<=pow(10,18):
        if t>1:a+=t-(a % t)
        t2=0
        s=str(a)
        for i in s:
            t2+=ord(i)-ord('0')
        if t2<=b:
            print(a-k)
            break
        t*=10
