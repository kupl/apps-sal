import sys
n=int(input())
z=list(map(int,input().split()))
z.append(91)
now=0
for i in z:
    if i-now>15:
        print(min(90, now+15))
        return
    else:
        now=i
print(90)
