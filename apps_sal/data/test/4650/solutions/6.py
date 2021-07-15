def ain():
    return map(int,input().split())
def lin():
    return list(ain())


def plist(l):
    for x in l:
        print(x, end= ' ')
    print()

def indexof(l,v,l3):
    return l3[v]


for _ in range(int(input())):
    n = int(input())
    l = lin()
    a=0
    b=0
    c=0
    for x in l:
        if x%3 == 0:
            a+=1
        elif x%3 == 1:
            b+=1
        else:
            c += 1
    s = a + min(b,c)
    if b > c:
        s += (b-c)//3
    else:
        s += (c-b)//3

    print(s)
