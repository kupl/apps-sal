a = input()
if len(a) // 2 * 2 == len(a):
    k = 1
    p = 0
else:
    k = 0
    p = 1
for i in range(k, len(a) // 2):
    b = a[:len(a) // 2 + i + p]
    c = a[len(a) // 2 - i:]
    if c == b:
        print('YES')
        print(c)
        break
else:
    print('NO')
