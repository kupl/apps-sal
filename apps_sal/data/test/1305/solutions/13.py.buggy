import sys


n = int(input())
a = list(map(int, input().split()))
d = dict()
d[25] = 0
d[50] = 0
for i in a:
    if i == 25:
        d[25] += 1
    elif i == 50:
        d[50] += 1
        if d[25] == 0:
            print("NO")
            return
        d[25] -= 1
    else:
        if d[25] == 0:
            print("NO")
            return
        elif d[50] == 0 and d[25] < 3:
            print("NO")
            return
        elif d[50] == 0:
            d[25] -= 3
        else:
            d[25] -= 1
            d[50] -= 1
print("YES")
