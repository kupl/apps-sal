#Dead
import math
sa3=[]
sa2=input().split(' ')
prime=int(sa2[0])
nums=int(sa2[1])
for x in range(nums):
    sa=int(input())
    sa3.append(sa)
sa4=[]
sa9001=0
for element in range(len(sa3)):
    sa5=sa3[element]%prime
    if sa5 in sa4 and sa9001!=1:
        print(element+1)
        sa9001=1
    else:
        sa4.append(sa3[element]%prime)
if sa9001==0:
    print(-1)

