n, t = map(int, input().split())
s = input()
for tem in range(0, t):
    s2 = ''
    cont = 0
    while cont < n - 1:
        if s[cont] == 'B' and s[cont + 1] == 'G':
            s2 += 'GB'
            cont += 2
        else:
            s2 += s[cont]
            cont += 1
    if cont == n - 1:
        s2 += s[-1]
    s = s2
print(s2)
