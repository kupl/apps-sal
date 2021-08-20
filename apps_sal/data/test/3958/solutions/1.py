(s, r, f, p) = (input(), [], 0, -1)
try:
    for i in range(len(s)):
        j = i + 1
        if s[i] == '0':
            if p > -1:
                r[p].append(j)
                p -= 1
            else:
                r.append([j])
        else:
            p += 1
            r[p].append(j)
except:
    f = 1
if f or p > -1:
    print(-1)
else:
    print(len(r))
    for x in r:
        print(len(x), *x)
