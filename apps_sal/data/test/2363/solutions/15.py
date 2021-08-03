def f(x, y): return f(y % x, x) + y // x if x else 0


I = input
for _ in '0' * int(I()):
    a, b = map(int, I().split())
    print(f(a, b))
