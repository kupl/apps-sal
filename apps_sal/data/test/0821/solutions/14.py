def chop():
    return (int(i) for i in input().split())
s,v1,v2,t1,t2=chop()
a1=s*v1+t1*2
a2=s*v2+t2*2
if a1==a2:
    print('Friendship')
elif a1<a2:
    print('First')
else:
    print('Second')

