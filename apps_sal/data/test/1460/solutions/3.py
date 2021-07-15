import sys
input = sys.stdin.readline

n=int(input())

ANS=[(0,0),(0,1),(1,0),(1,1)]

for i in range(n):
    ANS.append((i+1,i+2))
    ANS.append((i+2,i+1))
    ANS.append((i+2,i+2))

print(len(ANS))
for x,y in ANS:
    print(x,y)

