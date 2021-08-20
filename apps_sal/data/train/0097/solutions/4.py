def gets(a):
    i = 0
    a = list(a)
    b = [0] * 100
    for j in a:
        b[ord(j) - ord('A')] += 1
    r = -1
    t = -1
    while b[i] == 0 and i < 26:
        i += 1
    for k in range(0, len(a)):
        if r == -1 and ord(a[k]) - ord('A') == i:
            b[i] -= 1
            while b[i] == 0 and i < 26:
                i += 1
        elif r == -1:
            t = k
            r = 0
        elif ord(a[k]) - ord('A') == i:
            r = k
    if r != -1 and t != -1:
        (a[t], a[r]) = (a[r], a[t])
    return ''.join(a)


for _ in range(int(input())):
    (a, b) = input().split()
    a = gets(a)
    if a < b:
        print(a)
    else:
        print('---')
