import sys
n = int(input())
a = int(input())
b = 0
while True:
    c = 0
    if (500*b + c) > n:
        print("No")
        break
    for i in range(a+1):
        if (500*b + c) == n:
            print("Yes")
            return
        c+=1
    b+=1

