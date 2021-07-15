n = int(input())
a = input().split()
now = -1
white = 0
black = 0
for i in range(n):
    if(int(a[i]) == 0):
        if(white > 0):
            if(now == -1):
                now = white
            elif(now != white):
                print("NO")
                return
        
        white = 0
        black += 1
    else:
        if(black > 0):
            if(now == -1):
                now = black
            elif(now != black):
                print("NO")
                return
        black = 0
        white += 1

if(white > 0):
    if(now == -1):
        now = white
    elif(now != white):
        print("NO")
        return

if(black > 0):
    if(now == -1):
        now = black
    elif(now != black):
        print("NO")
        return
        
print("YES")
