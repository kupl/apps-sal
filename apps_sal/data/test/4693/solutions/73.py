# s=int(input())
# b=input()
# c=[]
# for i in range(b):
#     c.append(a[i])
a = list(map(int,input().split()))
#b = list(map(int,input().split()))

if (a[0]+a[1])<10:
    print(a[0]+a[1])
else:
    print("error")
