# import math
# import statistics
a=input()
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(i)
#e1,e2 = map(int,input().split())
#f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
# zoro = int(a[0]*len(a))
zyun= len(a)*9+int(a[0])
zoro=0
z = zyun//9
af= zyun%9
if af==0:
    if int(a)<=int(str(9)*(z-1)):
        print((int(str(9)*(z-1))))
    else:
            print((str(1)*(z)))
else :
    if int(a)<=int(str(af)*(z)):
        print((int(str(af)*(z))))
    else:
        print((int(str(af+1)*(z))))



