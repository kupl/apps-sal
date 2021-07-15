k = int(input())
keta = 1
ima = 1
def sunuke(n) :
    a = 0
    for i in str(n) :
        a += int(i)
    return(n/a)
count = 0
while count < k :
    if sunuke(ima) <= sunuke(ima+keta) :
        print(ima)
        ima += keta
        count += 1
    else :
        ima += 9*keta
        keta *= 10
