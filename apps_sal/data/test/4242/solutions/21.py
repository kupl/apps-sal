a,b,k = map(int,input().split())
li = []
def cf(a,b):
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            li.append(i)
    return li

cf(a,b)
li.insert(0,1)
li.reverse()
print(li[k-1])
