s=input().split()
n=int(s[0])
m=int(s[1])
mn=100000000

for i in range(m):
    str=input().split()
    if int(str[1])-int(str[0])<mn:
        mn=int(str[1])-int(str[0])

print(mn+1)

for i in range(n):
    print(i%(mn+1),end=" ")

