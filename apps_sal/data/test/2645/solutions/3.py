S = input()
p = 0
g = 0
a = 0
for s in S:
    if s == 'p':
        if p + 1 <= g:
            a += 0
            p += 1
        else:
            a -= 1
            g += 1
    elif p + 1 <= g:
        a += 1
        p += 1
    else:
        a += 0
        g += 1
print(a)
