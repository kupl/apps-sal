#s=int(input())
# b=input()
# c=[]
# for i in range(b):
#     c.append(a[i])
a = list(map(int,input().split()))
#b = list(map(int,input().split()))
c=0
for i in range(2):
    c+=a[a.index(max(a))]
    a[a.index(max(a))]=a[a.index(max(a))]-1

print(c)


