a = list(input())
b = list(input())
for i in range(0, len(a) + len(b)):
    if i % 2 == 0:
        print(a.pop(0), end='')
    else:
        print(b.pop(0), end='')
