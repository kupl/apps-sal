def magicOne(longest):
    count=0
    for side2 in range (2,longest+1):
        other = longest ^ side2
        if other <= side2 and other+side2>longest:
            count += 1
    return count

def magicXor(n):
    count=0;
    for i in range(1, n+1):
        count += magicOne(i)
    return count

def test():
    print(magicXor(6)==1)
    print(magicXor(10)==2)

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

print(magicXor(ni()))

