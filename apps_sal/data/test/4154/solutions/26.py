# import math
# import statistics
# a=input()
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(i)
e1, e2 = list(map(int, input().split()))
#f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
h = []
for i in range(e2):
    h.append(list(map(int, input().split())))
L = []
R = []
for i in range(len(h)):
    L.append(h[i][0])
for i in range(len(h)):
    R.append(h[i][1])

if min(R) >= max(L):
    print((min(R) - max(L) + 1))
else:
    print((0))
