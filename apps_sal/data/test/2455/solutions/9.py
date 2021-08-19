n = int(input())
p = 0
f = True
for k in range(n):
    s = input().strip()
    ot = set()
    for i in range(1, 13):
        if i == 5 or i == 7 or i == 9 or (i == 10) or (i == 11) or (i == 8):
            continue
        for t in range(i):
            p = True
            for j in range(t, 12, i):
                if s[j] == 'O':
                    p = False
            if p:
                ot.add(i)
    ot = list(reversed(sorted(list(ot))))
    print(len(ot), end=' ')
    for i in ot:
        print(str(12 // i) + 'x' + str(i), end=' ')
    print()
