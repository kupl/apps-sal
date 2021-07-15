s,p = list(map(int,input().split()))
import sys
for i in range(1,int(p**0.5)+1):
    m=s-i
    if i*m==p:
        print("Yes")
        return
print("No")

