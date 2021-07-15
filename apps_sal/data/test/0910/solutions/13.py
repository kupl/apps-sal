n, a, b = map(int, input().split())
if n > a * b:
    print(-1)
else:
    data = [[ i + 1 + b * j for i in range(b)][::pow(-1, j)] for j in range(a)]
    for i in range(a):
        for j in range(b):
            if data[i][j] > n:
                print(0, end=' ')
            else:
                print(data[i][j], end=' ')
        print()
