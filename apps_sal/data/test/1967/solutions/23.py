w,h=(int(x) for x in input().split(' '))
massive=[]
for i in range(h):
    mass=[]
    for elem in input(): 
        mass.append(elem)
        mass.append(elem)
    massive.append(mass)
    massive.append(mass)


    
for i in range(2*w):
    for j in range(2*h):
        print(massive[j][i],end='')
    print()
        

