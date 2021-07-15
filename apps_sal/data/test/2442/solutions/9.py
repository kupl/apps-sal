for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    a1 = 200
    a2 = 200
    for i in range(200, -1, -1):
        if l.count(i) < 2:
            a2 = i
        if l.count(i) < 1:
            a1 = i
    print(a1+a2)

