def same(a, b):
    L = [0] * 26
    for i in a:
        L[ord(i) - 97] += 1
    for i in b:
        L[ord(i) - 97] -= 1
    if L == [0] * 26:
        return True
    return False


for i in ' ' * int(input()):
    p = input()
    h = input()
    if len(p) > len(h):
        print('NO')
    else:
        c = 0
        for j in range(len(h) - len(p) + 1):
            s = h[j:j + len(p)]
            if same(p, s):
                c = 1
        if c:
            print('YES')
        else:
            print('NO')
