from sys import *
for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().rstrip().split()))
    l = list(map(int, stdin.readline().split()))
    k = []
    c = 0
    for x in range(a):
        if l[x] & 1 != 0:
            k.append(x + 1)
            c += 1
    j = c
    if j < b:
        print("NO")
    else:
        t = j - b
        if t & 1 == 0:
            print("YES")
            for x in range(b - 1):
                print(k[x], end=" ")
            print(a)
        else:
            print("NO")
