import sys

n=int(input())
CS=[list(input().split()) for i in range(n)]

LIST=[10**6]*7#A,B,C,AB,BC,AC,ABC


for cs in CS:
    if "A" in cs[1]:
        LIST[0]=min(LIST[0],int(cs[0]))
    if "B" in cs[1]:
        LIST[1]=min(LIST[1],int(cs[0]))
    if "C" in cs[1]:
        LIST[2]=min(LIST[2],int(cs[0]))
    if "A" in cs[1] and "B" in cs[1]:
        LIST[3]=min(LIST[3],int(cs[0]))
    if "B" in cs[1] and "C" in cs[1]:
        LIST[4]=min(LIST[4],int(cs[0]))
    if "C" in cs[1] and "A" in cs[1]:
        LIST[5]=min(LIST[5],int(cs[0]))
    if "A" in cs[1] and "B" in cs[1] and "C" in cs[1]:
        LIST[6]=min(LIST[6],int(cs[0]))

if LIST[0]==10**6 or LIST[1]==10**6 or LIST[2]==10**6:
    print(-1)

else:
    print(min(LIST[0]+LIST[1]+LIST[2],LIST[0]+LIST[4],LIST[1]+LIST[5],LIST[2]+LIST[3],LIST[6]))

