n, a, b = map(int, input().split())
if a * b < n:
    print(-1)
else:
    for i in range(a):
        if b % 2 == 1 or i % 2 == 0:
            for j in range(1, b + 1):
                k = b * i + j
                if k > n:
                    k = 0
                print(k, end=' ')
            print(' ')
        else:
            for j in range(b, 0, -1):
                k = b * i + j
                if k > n:
                    k = 0
                print(k, end=' ')
            print(' ')
