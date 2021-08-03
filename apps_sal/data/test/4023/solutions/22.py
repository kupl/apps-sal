n = int(input())
a = list(map(int, input().split()))
b = [0] * 1000000
sp = -1
max = 0
f = True
for i in range(n):
    sp = sp + 1
    b[sp] = a[i]
    if b[sp] > max:
        max = b[sp]
    if sp > 0:
        if b[sp] > b[sp - 1]:
            f = False

        if b[sp] == b[sp - 1]:
            sp = sp - 2

if f == True:
    if sp == 0:
        if b[sp] >= max:
            print("YES")
        else:
            print("NO")

    elif sp < 0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")
