t = int(input())
for you in range(t):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    x = max(a, b)
    y = min(a, b)
    if x > 2 * y:
        print(y)
    else:
        print((x + y) // 3)
