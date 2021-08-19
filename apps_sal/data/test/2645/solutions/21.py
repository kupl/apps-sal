s = input()
p = 0
g = 0
res = 0
for i in range(len(s)):
    if s[i] == 'g':
        if p < g:
            p += 1
            res += 1
        else:
            g += 1
    elif p < g:
        p += 1
    else:
        g += 1
        res -= 1
print(res)
