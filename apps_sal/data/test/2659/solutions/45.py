#D問題
K=int(input())
keta=1
now=1
count=0

def sunuke(n):
    a=0
    for i in str(n):
        a+=int(i)
    return(n/a)

while count < K:
    if sunuke(now) <= sunuke(now+keta):
        print(now)
        now+=keta
        count+=1
    else:
        now+=9*keta
        keta*=10


