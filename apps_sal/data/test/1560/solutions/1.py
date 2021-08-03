def fbf():
    bbad = 0
    rbad = 0
    for i in range(n):
        if (i % 2 == 0 and a[i] == 'r'):
            rbad += 1
        if (i % 2 == 1 and a[i] == 'b'):
            bbad += 1
    return max(bbad, rbad)


def frf():
    bbad = 0
    rbad = 0
    for i in range(n):
        if (i % 2 == 1 and a[i] == 'r'):
            rbad += 1
        if (i % 2 == 0 and a[i] == 'b'):
            bbad += 1
    return max(bbad, rbad)


n = int(input())
a = input()
print(min(fbf(), frf()))
