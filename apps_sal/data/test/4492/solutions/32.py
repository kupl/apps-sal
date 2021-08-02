def boxes():
    N, x = input().split()
    N, x = int(N), int(x)
    arr = [int(a) for a in input().split()]

    total = 0
    for i in range(1, N):
        a, b = arr[i - 1], arr[i]
        extra = a + b - x
        if extra > 0:
            total += extra
            if b >= extra:
                arr[i] -= extra
            else:
                arr[i] = 0
    print(total)


boxes()
