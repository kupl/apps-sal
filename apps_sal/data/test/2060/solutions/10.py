t = int(input())
for i in range(t):
    n = int(input())
    f = 0
    for i in range(0, 101):
        for j in range(0, 101):
            if i * 3 + j * 7 == n:
                print("YES")
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print("NO")
