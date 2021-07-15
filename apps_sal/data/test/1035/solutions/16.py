import math
a,b = (int(x) for x in input().split())
saidai = 1

def yakusuu(x,y):
    return(y,x % y)

def cont(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

saidai = math.gcd(a,b)


d = cont(saidai)
if d[0] == [1,1]:
    print((1))
    return
print((len(d) + 1))

