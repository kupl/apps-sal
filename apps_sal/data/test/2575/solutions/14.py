p = int(input())
while p:
    n = int(input())
    if 360 % (180 - n) == 0: print("YES")
    else: print("NO")
    p -= 1
