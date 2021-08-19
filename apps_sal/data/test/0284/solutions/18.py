n = int(input())
ok = False
i = 0
while i * 1234567 <= n:
    j = 0
    while i * 1234567 + j * 123456 <= n:
        x = i * 1234567 + j * 123456
        if (n - x) % 1234 == 0:
            ok = True
            break
        j += 1
    if ok:
        break
    i += 1
print('YES' if ok else 'NO')
