

n = int(input())

for _ in range(n):
    x = int(input())
    found = False
    a = 0
    while a * 7 <= x:
        if (x - a * 7) % 3 == 0:
            found = True
            break
        a += 1
    if found:
        print("YES")
    else:
        print("NO")
