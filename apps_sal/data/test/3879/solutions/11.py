n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])
    while(l[i] % 2 == 0):
        l[i] /= 2
    while(l[i] % 3 == 0):
        l[i] /= 3
flag = 1
for i in range(n):
    if(l[i] != l[0]):
        print("No")
        flag = 0
        break
if(flag):
    print("Yes")
