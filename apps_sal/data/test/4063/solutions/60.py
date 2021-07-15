import math
import statistics
a=int(input())
#b=int(input())
# c=[]
# for i in b:
#     c.append(i)
# e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
#j = [input() for _ in range(3)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
f.sort()
tyu = statistics.median(f)
if f[len(f)//2]==f[len(f)//2-1]:
    print(0)
else:
    print(f[len(f)//2]-f[len(f)//2-1])
