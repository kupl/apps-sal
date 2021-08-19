# import math
# import statistics
a = input()
# b,c=int(input()),int(input())
c = []
for i in a:
    c.append(i)
#e1,e2,e3,e4 = map(int,input().split())
#f = list(map(int,input().split()))
#g = [input() for _ in range(a)]

d = set(c)

if len(d) < len(c):
    print("no")
else:
    print("yes")
