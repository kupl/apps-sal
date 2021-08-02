def f():
    t = []
    for i in range(8):
        p = input()
        for j in range(8):
            if p[j] == 'K': t += [i, j]
    if t[2] - t[0] in (0, 4) and t[1] - t[3] in (-4, 0, 4): return 'YES'
    return 'NO'


for i in range(int(input()) - 1):
    print(f())
    input()
print(f())
