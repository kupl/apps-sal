def read():
    return list(map(int,input().split()))
n=int(input())
a=read()
B=0
C=0
for i in a:
    if i>0:
        B+=i
    else:
        C+=i
print(B-C)

