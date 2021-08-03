for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    e = 0
    o = 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            if (i % 2):
                e += 1
            else:
                o += 1
    if o == e:
        print(o)
    else:
        print(-1)
