n = input()
y = int(n)

if y < 10:
    print(1)
else:
    l = len(n)
    f = int(n[0]) + 1
    f *= 10 ** (l - 1)
    print(f - y)
