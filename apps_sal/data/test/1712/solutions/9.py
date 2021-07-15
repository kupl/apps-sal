n, x, y = list(map(int, input().split()))
for _ in range(n):
    a = int(input())
    c1, c2 = ((a + 1) * x // (x + y)) / x, ((a + 1) * y // (x + y)) / y
    if c1 == c2:
        print('Both')
    elif c1 > c2:
        print('Vanya')
    else:
        print('Vova')

