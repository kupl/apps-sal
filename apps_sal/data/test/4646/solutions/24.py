for _ in range(int(input())):
    input()
    l = list(map(int, input().split()))
    e = 0
    o = 0
    for i in range(len(l)):
        if l[i] % 2 != i % 2:
            if i % 2 == 0:
                e += 1
            else:
                o += 1
    print(-1 if e != o else e)
