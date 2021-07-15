import sys
import math
input = sys.stdin.readline

testcase=int(input())
T=[list(map(int,input().split())) for i in range(testcase)]

def bi(n,k):
    MIN=0
    MAX=n

    while MAX>MIN+1:
        bn=(MIN+MAX)//2
        if math.log2(k+2+bn)<bn+1:
            MAX=bn
        elif math.log2(k+2+bn)==bn+1:
            return bn
        else:
            MIN=bn

    if MAX+1<=math.log2(k+2+MAX):
        return MAX

    return MIN

for n,k in T:
    if n==1:
        if k==1:
            print("YES",0)
        else:
            print("NO")
        continue

    if n==2:
        if 1<=k<=2:
            print("YES",1)
        elif k==3:
            print("NO")
        elif 4<=k<=5:
            print("YES",0)
        else:
            print("NO")
        continue
        
    if n<=30 and k>(pow(4,n)-1)//3:
        print("NO")
        continue

    ANS=bi(n,k)

    print("YES",n-ANS)
    
    

