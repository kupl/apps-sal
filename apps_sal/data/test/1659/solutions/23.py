n,x = map(int,input().split())
pres = x
dis = 0
for i in range(n):
    a,b = input().split()
    b = int(b)
    if(a=='+'):
        pres += b
    else:
        if(pres<b):
            dis += 1
        else:
            pres -= b
print(pres,dis)
