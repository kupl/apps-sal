T = int(input())
for __ in range(T):
    n = int(input())
    s = input()
    ok = all((c in '-<') for c in s) or all((c in '->') for c in s)
    cnt = 0
    for i in range(n):
        j = (i + 1) % n
        c1, c2 = s[i], s[j]
        if c1 == '-' or c2 == '-':
            cnt += 1
        else:
            cnt += (1 if ok else 0)
    print(cnt)
