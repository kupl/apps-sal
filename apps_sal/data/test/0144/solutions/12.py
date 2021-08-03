n = int(input())
s = input()
su = 0
for i in s:
    su += int(i)
tr = 0
if (su == 0):
    print("YES")
else:
    for i in range(1, su):
        if (su % i == 0):
            t = 0
            x = 1
            for c in s:
                if (t + int(c) == i):
                    t = 0
                elif(t + int(c) > i):
                    x = 0
                else:
                    t += int(c)
            if(x == 1):
                tr = 1
    if (tr == 1):
        print("YES")
    else:
        print("NO")
