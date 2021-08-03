t = int(input())
ans = [[] for i in range(t)]
for i in range(t):

    s = input()
    for a in range(1, 13):

        if 12 % a != 0:
            continue
        b = 12 // a
        c = [[] for h in range(b)]
        for h in range(b):
            for k in range(a):
                c[h].append(s[k * b + h])
        if a == 3:
            a = 3
        T = True
        for h in range(b):
            if T:
                ok = True
                for k in range(a):
                    if c[h][k] == 'O':
                        ok = False
                if ok:
                    ans[i].append([a, b])
                    T = False
                    break
for i in range(t):
    print(len(ans[i]), end=' ')
    for z in ans[i]:
        print(z[0], end='')
        print('x', end='')
        print(z[1], end=' ')
    print()
