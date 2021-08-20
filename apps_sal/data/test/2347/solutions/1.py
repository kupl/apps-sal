n = int(input())
for i in range(n):
    p = input()
    h = input()
    p = sorted(p)
    good = False
    for i in range(len(h)):
        if i + len(p) > len(h):
            break
        if sorted(h[i:i + len(p)]) == p:
            good = True
    if good:
        print('YES')
    else:
        print('NO')
