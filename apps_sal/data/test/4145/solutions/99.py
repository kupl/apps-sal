import sys

x=int(input())


for x in range(x,x*2):
        for i in range(2,x//2):
                if x%i==0:
                        break
        else:
                print(x)
                return
