def genstring(num, length, index):
    return ('0 ' * index + str(num) + ' ' + '0 ' * (length - index)).strip()


(a, b) = list(map(int, input().split(' ')))
for t in range(a):
    print(genstring(b, a - 1, t))
