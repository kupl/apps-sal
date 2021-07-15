import math
# s=int(input())
# b=input()
# c=[]
# for i in range(b):
#     c.append(a[i])
a = list(map(int,input().split()))
#b = list(map(int,input().split()))

if a[0]+a[1]<a[2]+a[3]:
    print("Right")
elif a[0]+a[1]==a[2]+a[3]:
    print("Balanced")
elif a[0]+a[1]>a[2]+a[3]:
    print("Left")
