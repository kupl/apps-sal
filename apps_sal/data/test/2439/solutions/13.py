
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    a.sort()
    s = 0
    for i in a:
        s += i
        if s == 0:
            break
    else:
        print("YES")
        print(*a)
        continue

    a.reverse()
    s = 0
    for i in a:
        s += i
        if s == 0:
            break
    else:
        print("YES")
        print(*a)
        continue

    print("NO")
