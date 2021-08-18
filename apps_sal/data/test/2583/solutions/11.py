import math
for nt in range(int(input())):
    n = int(input())
    if n == 1:
        print("FastestFinger")
        continue
    elif n == 2:
        print("Ashishgup")
        continue
    if n % 2:
        print("Ashishgup")
        continue
    x = 0
    m = n
    while n % 2 == 0:
        n = n // 2
        x += 1
    if n == 1:
        print("FastestFinger")
        continue
    if x == 1:
        left = m // 2
        flag = 0
        for i in range(2, int(left**0.5) + 1):
            if left % i == 0:
                flag = 1
                break
        if flag:
            print("Ashishgup")
        else:
            print("FastestFinger")
    else:
        print("Ashishgup")
