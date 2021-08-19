def f(n):
    return n // 7 + (n + 1) // 7


try:
    while True:
        n = int(input())
        if n == 1:
            print('0 1')
        else:
            print(f(n), 2 + f(n - 2))
except EOFError:
    pass
