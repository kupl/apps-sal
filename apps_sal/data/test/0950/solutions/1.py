(n, m) = list(map(int, input().split()))
char = [m * 100] * n
dig = [m * 100] * n
symb = [m * 100] * n
for i in range(n):
    s = input()
    for (j, c) in enumerate(s):
        if c in '*#&':
            symb[i] = min(symb[i], j, m - j)
        elif c.isdigit():
            dig[i] = min(dig[i], j, m - j)
        else:
            char[i] = min(char[i], j, m - j)
answer = m * 100
for c in range(n):
    for s in range(n):
        for d in range(n):
            if len(set([c, s, d])) == 3:
                answer = min(answer, char[c] + symb[s] + dig[d])
print(answer)
