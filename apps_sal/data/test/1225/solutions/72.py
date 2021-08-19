def f(h):
    if h != 1:
        return f(h // 2) * 2 + 1
    else:
        return 1


h = int(input())
print(f(h))
