n, k = map(int,input().split())

if k % 2 == 1:
    x = 0
    for i in range(1,n+1):
        if i % k == 0:
            x += 1
    print(x**3)
else:
    x = 0
    for i in range(1,n+1):
        if i % k == 0:
            x += 1
    y = 0
    for i in range(1,n+1):
        if i % k == k//2:
            y += 1
    print(x**3 + y**3)
