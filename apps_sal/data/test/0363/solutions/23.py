n = input()
k = 9
l = len(n)
if l == 1:
    print(n)
else:
    c = (int(n) - int('9' * (l - 1))) * l
    for i in range(l - 1):
        c += k * (i + 1)
        k *= 10
    print(c)
