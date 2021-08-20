while 1:
    try:
        (y, k, n) = map(int, input().split())
        start = y // k
        end = n // k
        if y >= n or start == end:
            print(-1)
        else:
            for i in range(start + 1, end + 1):
                print(k * i - y, end=' ')
            print('')
    except EOFError:
        break
