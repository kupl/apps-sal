from sys import stdin

n=int(input())
bus=[]
possible=False
for i in range(n):
    rangee=list(input())
    if not possible and rangee[0]=='O' and rangee[1]=='O':
        possible=True
        rangee[0]='+'
        rangee[1]='+'
    elif not possible and rangee[-1]=='O' and rangee[-2]=='O':
        possible=True
        rangee[-1]='+'
        rangee[-2]='+'
    bus.append(rangee)

if possible:
    print("YES")
    for i in range(n):
        print(*bus[i],sep="")
else:
    print("NO")

