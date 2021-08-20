t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    o = 0
    z = 0
    for i in range(n):
        if l[i]:
            o += 1
        else:
            z += 1
    if o > z:
        o -= o % 2
        print(o)
        for i in range(o):
            print(1, end=' ')
    else:
        print(z)
        for i in range(z):
            print(0, end=' ')
    print()
