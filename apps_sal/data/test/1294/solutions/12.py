t = int(input())

for _ in range(t):
    s = input() + '-'
    ok = {c: False for c in 'qwertyuiopasdfghjklzxcvbnm'}
    cur = 0
    p = ''
    for c in s:
        if c == p:
            cur += 1
        else:
            if cur % 2:
                ok[p] = True
            cur = 1
            p = c
    for c, f in sorted(ok.items()):
        if f:
            print(c, end='')
    print()
