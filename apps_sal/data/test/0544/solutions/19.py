def getV(c):
    if (c == 'a'):
        return ['b']
    if (c == 'z'):
        return ['y']
    return [chr(ord(c) + 1), chr(ord(c) - 1)]


T = int(input().strip())

for i in range(T):
    n = int(input().strip())
    s = input().strip()
    for j in range(n // 2):
        first = getV(s[j])
        second = getV(s[n - j - 1])
        b = False
        for c in second:
            if c in first:
                b = True
                break
        if not (b):
            print('NO')
            break
    else:
        print('YES')
