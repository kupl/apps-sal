n = int(input())
sq = [None]  * 51
sqsum  = 0
for i in range(n):
    sq[i]= list(map(int,input().split()))
    sqsum+=(sq[i][3]-sq[i][1])*(sq[i][2]-sq[i][0])
maxx = max(map(lambda x:x[2],sq[:n]))
minx = min(map(lambda x:x[0],sq[:n]))
maxy = max(map(lambda x:x[3],sq[:n]))
miny =  min(map(lambda x:x[1],sq[:n]))
area = (maxy-miny)*(maxx-minx)

if maxx-minx!=maxy-miny or area!=sqsum:
    print("NO")
else:
    print("YES")
