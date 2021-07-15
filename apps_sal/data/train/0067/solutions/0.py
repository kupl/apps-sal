for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()

    d = {}
    for i in range(ord('a'), ord('z') + 1):
        d[chr(i)] = 0

    for cs in s:
        d[cs] += 1
    for ct in t:
        d[ct] += 1

    ok = True
    for e in d:
        if d[e] % 2 == 1:
            ok = False

    if not ok:
        print("No")
    else:
        print("Yes")

        changes = []

        s, t = list(s), list(t)
        for i in range(n-1):
            if s[i] != t[i]:
                r = (0, -1)
                for j in range(i+1, n):
                    if s[j] == t[i]:
                        r = (j, 0)

                for j in range(i+1, n):
                    if t[j] == t[i]:
                        r = (j, 1)

                if r[1] == 0:
                    changes += [(r[0], i+1), (i, i+1)]
                    s[r[0]], t[i+1] = t[i+1], s[r[0]]
                    s[i], t[i+1] = t[i+1], s[i]
                elif r[1] == 1:
                    changes += [(i, r[0])]
                    s[i], t[r[0]] = t[r[0]], s[i]

        print(len(changes))
        for change in changes:
            x, y = change
            print(x+1, y+1)
