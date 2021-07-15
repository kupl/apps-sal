n,l=[int(x) for x in input().split(' ')]
locations=[int(x) for x in input().split(' ')]
locations=sorted(locations)
# print(locations)
minimum=0
a=0
b=1
while b<n:
    # print(minimum)
    minimum=max(minimum,(locations[b]-locations[a])/2)
    # print(" became ",minimum)
    a+=1
    b+=1
minimum=max(minimum,locations[0],l-locations[-1])
print(minimum)

