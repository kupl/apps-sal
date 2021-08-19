def check(x):
    while (x > 1):
        if (x % 2 == 0):
            x /= 2
        elif (x % 3 == 0):
            x /= 3
        else:
            return False
    return True


a = []
n = int(input())
a = list(map(int, input().split()))
a.sort()
flag = True
while (a[0] % 2 == 0 or a[0] % 3 == 0):
    if(a[0] % 2 == 0):
        a[0] /= 2
    else:
        a[0] /= 3
#print (a)
for x in a:
    y = x % a[0]
    z = x / a[0]
    #print (y,z)
    if(y == 0 and check(z)):
        continue
    else:
        flag = False
if flag == True:
    print('Yes')
else:
    print('No')
