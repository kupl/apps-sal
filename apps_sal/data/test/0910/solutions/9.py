(n, a, b) = map(int, input().split())
s = a * b
if s < n:
    print(-1)
elif b % 2 == 1:
    for i in range(a):
        for j in range(b):
            x = i * b + j + 1
            if x > n:
                print(0, end=' ')
            else:
                print(x, end=' ')
        print()
else:
    for i in range(a):
        for j in range(b):
            x = i * b + j + 1
            if i % 2 == 1:
                x = i * b + b - j
            if x > n:
                print(0, end=' ')
            else:
                print(x, end=' ')
        print()
