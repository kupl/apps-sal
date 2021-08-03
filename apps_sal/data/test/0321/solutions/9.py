import math
t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    if((a - b) != 1):
        print("NO")
    else:
        l = 2 * a - 1
        p = 0
        for k in range(2, int(math.sqrt(l)) + 1):
            if(l % k == 0):
                print("NO")
                p = 1
                break
        if(p == 0):
            print("YES")
