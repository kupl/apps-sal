a = list(map(int,input().split()))
#b = list(map(int,input().split()))

h = 0
p = 1
li = []

for i in range(999):
    h +=p
    p +=1
    li.append(h)

for i in range(len(li)):
    for k in range(len(li)):
        if (a[0]-li[i])==(a[1]-li[k]) and k == i+1:
            print((abs(a[0]-li[i])))
            


