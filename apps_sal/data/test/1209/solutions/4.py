import math
a = int(input())
li = []
b = 0
for i in range(a):
    k = float(input())
    if k == int(k):
        b += 1
        li.append(int(k))
    else:
        k = math.floor(k)
        if k < 0:
            li.append(k - 0.00000000001)
        else:
            li.append(k + 0.00000000001)
ans = 0
for i in li:
    ans += int(i)
if ans == 0:
    print(*li)
else:
    for i in li:
        if (ans < 0):
            if i == int(i):
                print(i)
            else:
                ans += 1
                print(int(i) + 1)
        else:
            print(int(i))
