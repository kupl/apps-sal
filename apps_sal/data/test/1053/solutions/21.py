f = lambda x: f(x // 2) * 2 + (x + 1) // 2 if x else 0
print(f(int(input()) - 1))
