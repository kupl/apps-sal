3.5
mas=[int(x) for x in input().split()]
mas.sort()

p=0
k=mas[2]-1

if mas[1]<k:
    p+=k-mas[1]
if mas[0]<k:
    p+=k-mas[0]
    
print(p)
