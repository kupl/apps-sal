c = int(input())
ans = 0
q = 0
m = [[i, 1] for i in 'abcdefghijklmnopqrstuvwxyz']
for i in range(c):
    suma = 0
    for j in range(26):
        suma += m[j][1]
    if suma < 2:
        q = 1
    x = input()
    a = set(x[2:])
    x = x[0]
    if x == '.':
        for j in range(26):
            if m[j][0] in a:
                m[j][1] = 0
    elif x == '!':
        for j in range(26):
            if not m[j][0] in a:
                m[j][1] = 0
        if q:
            ans += 1
    else:
        for j in range(26):
            if m[j][0] in a:
                m[j][1] = 0
        if i != c - 1 and q:
            ans += 1
print(ans)
