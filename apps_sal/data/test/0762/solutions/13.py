from math import ceil

t = 1
for test in range(t):
    n,b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    countOdd = 0
    countEven = 0
    cuts = []
    prev = 0
    for i in a:
        if countEven==countOdd:
            cuts.append(abs(prev-i))
        if i%2 == 0:
            countEven+=1
        else:
            countOdd+=1
        prev = i
    cuts[0] = 200 #useless
    cuts.sort()
    ans=0
    cost = 0
    for i in cuts:
        if cost+i>b:
            break
        else:
            ans+=1
            cost+=i
    print(ans)

