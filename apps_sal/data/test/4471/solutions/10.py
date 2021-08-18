for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    e = 0
    o = 0
    for t in l:
        if t % 2:
            o += 1
        else:
            e += 1
    if not e or not o:
        print("YES")
    else:
        print("NO")
