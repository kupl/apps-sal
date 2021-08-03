x = int(input()) + 1
c = 1


def has_eight(x):
    return '8' in str(x)


while not has_eight(x):
    x += 1
    c += 1

print(c)
