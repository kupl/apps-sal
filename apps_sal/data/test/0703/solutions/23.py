otseki, nuts, raz, vmest = list(map(int, input().split()))
maxbox = vmest * otseki
boxes = 0
curbox = vmest

while nuts > 0:

    if curbox < maxbox and raz > 0:
        curbox += vmest
        raz -= 1
    else:
        nuts -= curbox
        curbox = vmest
        boxes += 1
#    print(nuts)
print(boxes)
