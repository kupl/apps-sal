N = int(input().split()[0])
a = [0,0,0,0]
for i in range(N):
    b=input().split()[0]
    if(b == 'AC'):
        a[0]+=1
    elif(b == 'WA'):
        a[1]+=1
    elif(b == 'TLE'):
        a[2]+=1
    elif(b == 'RE'):
        a[3]+=1
print(("AC x {0}\nWA x {1}\nTLE x {2}\nRE x {3}".format(a[0],a[1],a[2],a[3])))

