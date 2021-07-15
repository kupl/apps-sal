def on(l1, l2):
    return(abs(l1[0]-l2[0])>=l1[1]+l2[1])
n = int(input())
inf = []
for i in range(n):
    a,b = list(map(int,input().split()))
    inf.append([a+b,a-b])
inf.sort()
res = 1
last = 0
for i in range(1,n):
    if inf[i][1] >= inf[last][0]:
        res+=1
        last = i
print(res)


