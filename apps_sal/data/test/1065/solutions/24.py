a = input()

a = a.split(' ')

for i in range(len(a)):
    a[i] = int(a[i])

def kandidati():
    d = []
    for i in range(1,a[3]):
        if a[0]//(i*a[1]+1) < a[2]:
            d += [(a[0]//(i*a[1]+1))*(i+1)]

    if a[0] % int(a[1]*a[2]) == 0:
        s = a[0]/(a[1]*a[2])
        d += [int(a[2]*s)]
    else:
        f = int(a[0]//(a[1]*a[2]))
        if  a[0] - f*a[2]*a[1] >= a[2]:
            s = a[0]//(a[1]*a[2])+1
        else:
            s = a[0]//(a[1]*a[2])
        d += [int(a[2]*s)]
    print(max(d))
        
kandidati()


