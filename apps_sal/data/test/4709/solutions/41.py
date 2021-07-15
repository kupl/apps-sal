def calculate(a, b, op):
    if op == '+':
        return a + b
    else:
        return a - b


lst = list(map(str, input().split()))
print(calculate(int(lst[0]), int(lst[2]), lst[1]))
