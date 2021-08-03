# import math
# import statistics
a = int(input())
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(i)
#e1,e2 = map(int,input().split())
f = list(map(int, input().split()))
#g = [input() for _ in range(a)]

count = 0
for i in range(a - 1):
    if f[i] != f[i + 1] - 1:
        f[i + 1] = i + 2
        count += 1
if count == 2 or count == 0:
    print("YES")
else:
    print("NO")
