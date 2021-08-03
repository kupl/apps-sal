q = [12, 6, 4, 3, 2, 1]
p = {12 // i: 'X' * i for i in q}
r = {i: str(12 // i) + 'x' + str(i) for i in q}
for i in range(int(input())):
    s, t = [], input()
    for j in q:
        if any(t[k:: j] == p[j] for k in range(j)):
            s.append(r[j])
    print(len(s), ' '.join(s))
