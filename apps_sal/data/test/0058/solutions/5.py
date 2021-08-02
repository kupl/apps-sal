n = int(input())
a = int(input())
b = int(input())
na = 4
nb = 2
cnt = 0
while True:
    len = n
    cnt += 1
    while len > 0:
        resa = len - min(int(len / a), na) * a
        resb = len - min(int(len / b), nb) * b
        if resa < resb and na > 0 and len >= a:
            len -= a
            na -= 1
        elif nb > 0 and len >= b:
            len -= b
            nb -= 1
        else:
            break
    if na == nb == 0:
        break
print(cnt)
