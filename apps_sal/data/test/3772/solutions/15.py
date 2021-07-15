def f(a, b):
    if a < b:
        return f(b, a)
    elif b == 1:
        return a
    else:
        return f(b, a%b) + a//b

(a, b) = map(int, input().split())

print(f(a, b))
