n = int(input())

for i in range(n):
    a = int(input())
    if(360 % (180 - a) == 0 and 360 // (180 - a) > 2):
        print("YES")
    else: print("NO")
