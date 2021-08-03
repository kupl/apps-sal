a, b = input().split(':')
a = int(a)
b = int(b)
anw = 0


def palin(s):
    return s == s[::-1]


while not palin(str(a).zfill(2) + str(b).zfill(2)):
    anw += 1
    b += 1
    if (b == 60):
        b = 0
        a += 1
    if (a == 24):
        a = 0

print(anw)
