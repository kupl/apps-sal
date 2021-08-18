def func():
    n = int(input())
    g = [()] + [set(map(int, input().split())) for i in range(n)]
    if n == 3:
        print(1, 2, 3)
        return None

    xor = [1]
    for i in range(n - 1):
        x, y = (j for j in g[xor[-1]])
        if x in g[y]:
            xor.append(y)
        elif y in g[x]:
            xor.append(x)
    print(' '.join(map(str, xor)))


func()
