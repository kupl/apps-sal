(s, t, i) = ({}, [], 1)
for n in range(int(input())):
    (c, a, b) = map(int, input().split())
    if c > 1:
        print('YES' if b in s[a] else 'NO')
    else:
        s[i] = [i]
        for (j, (x, y)) in enumerate(t, 1):
            if x < a < y or x < b < y:
                s[i].extend(s[j])
        s[i] = set(s[i])
        r = [j for (j, (x, y)) in enumerate(t, 1) if a < x < b or a < y < b]
        for j in range(1, len(t) + 1):
            if any((k in s[j] for k in r)):
                s[j].update(s[i])
        t.append((a, b))
        i += 1
