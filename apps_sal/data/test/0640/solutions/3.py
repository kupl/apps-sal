in_put=input().split(' ')
first=int(in_put[0])
second=int(in_put[1])
win=[]
draw=[]
lose=[]
for x in range(1, 7):
    if abs(x-first)<abs(x-second):
        lose.append(x)
    elif abs(x-first)>abs(x-second):
        win.append(x)
    else:
        draw.append(x)
print(str(len(lose))+' '+str(len(draw))+' '+str(len(win)))

