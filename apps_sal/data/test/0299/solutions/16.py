import sys

n = int(sys.stdin.readline())
l = [int(x) for x in (sys.stdin.readline()).split()]

chest = 0
biceps = 0
back = 0

i = 0
while(i < n):
    chest += l[i]
    i += 3
    
i = 1
while(i < n):
    biceps += l[i]
    i += 3
    
i = 2
while(i < n):
    back += l[i]
    i += 3
    
if(chest >= biceps and chest >= back):
    print("chest")
elif(biceps > chest and biceps > back):
    print("biceps")
elif(back > biceps and back > chest):
    print("back")
