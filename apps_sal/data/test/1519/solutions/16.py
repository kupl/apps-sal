def mainA():
    n, L, a = list(map(int, input().split()))
    times = 0
    begin = 0
    for i in range(n):
        b, c = list(map(int, input().split()))
        times += (b - begin) // a
        begin = b + c
    times += (L - begin) // a
    print(times)

mainA()

