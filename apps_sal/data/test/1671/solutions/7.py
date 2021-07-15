n=int(input())
a=[int(i) for i in input().split()]
a.sort()
Yu=sum(a)%n
pin=sum(a)//n
re=0

for i in a:
    if i<pin:
        re+=pin-i
    else:
        break

if Yu==0:
    print(re)
else:
    re_2=0
    for i in a:
        if i <=pin+1:
            continue
        else:
            re_2+=i-pin-1
    print(max(re,re_2))
            

