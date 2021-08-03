import math
# b=input()
# c=[]
# for i in range(b):
#     c.append(a[i])
a = list(map(int, input().split()))
#b = list(map(int,input().split()))
s = int(input())

for i in range(s):
    a[a.index(max(a))] = a[a.index(max(a))] * 2

print(sum(a))
