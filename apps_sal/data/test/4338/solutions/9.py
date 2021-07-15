n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
if x > y:
    print(n)
else:
    b = 0
    for i in a:
        if i <= x:
            b += 1
    if b % 2:
        print(b // 2 + 1)
    else:
        print(b // 2)

