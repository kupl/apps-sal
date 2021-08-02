input()
intro = sorted([(-x, i + 1) for i, x in enumerate(map(int, input().split()))])
extro = []
line = input()
sol = []
for c in line:
    if c == '0':
        w, r = intro.pop()
        extro.append((w, r))
        sol.append(str(r))
    else:
        w, r = extro.pop()
        sol.append(str(r))
print(' '.join(sol))
