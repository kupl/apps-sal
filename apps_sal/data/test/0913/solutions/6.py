input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ex1 = sum((i & ~j for (i, j) in zip(a, b)))
ex2 = sum((j & ~i for (i, j) in zip(a, b)))
try:
    print(ex2 // ex1 + 1)
except ZeroDivisionError:
    print(-1)
