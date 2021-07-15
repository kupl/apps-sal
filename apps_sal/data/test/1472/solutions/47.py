n,x,y = list(map(int,input().split()))

dis_list = [0]*(n)

for start in range(1,n+1):
    for end in range(start+1,n+1):
        dis1 = end - start
#        dis2 = (end-start) - (y-(x+1))
        dis3 = abs(x-start)+abs(y-end)+1
        a = min(dis1,dis3)
        dis_list[a] += 1


for i in range(1,n):
    print((dis_list[i]))

