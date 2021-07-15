a = [int(i) for i in input().split()]
flag=False
d1 = a[1]-a[0]
d2 = a[2]-a[1]
d3 = a[3]-a[2]
q1 = a[1]/a[0]
q2 = a[2]/a[1]
q3 = a[3]/a[2]
if(d1==d2==d3):
    print(a[3]+d1)
    flag=True
elif(q1==q2==q3):
    otv = a[3]*q1-(int(a[3]*q1))
    tmp = 0 + otv
    if(tmp<=0):
        print(int(a[3]*q1))
        flag=True
if(flag==False):
    print('42')
