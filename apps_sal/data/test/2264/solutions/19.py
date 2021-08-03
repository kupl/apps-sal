for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = list(map(int, input().split()))
        a.append(ai)
        b.append(bi)
    if n == 1:
        print(0)
    else:
        if max(a) < min(b):
            print(0)
        else:
            print(max(a) - min(b))
