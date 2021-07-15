n = int(input())


d = []
for _ in range(n):
    s1 = input()
    s2 = ""
    for c in s1:
        if c in ('a', 'e', 'o', 'i',  'u'):
            s2 += c

    d.append((len(s2), s2[-1], s1))


d.sort(key=lambda x: (x[0], x[1]))

r = []

ost = []
p_a, p_b, p_c = 0, '', ''
for a, b, c in d:
    if a == p_a and b == p_b:
        r.append([p_c, c])
        p_a, p_b, p_c = 0, '', ''
        continue
    if p_a != 0:
        ost.append((p_a, p_b, p_c))
    p_a, p_b, p_c = a, b, c

if p_a != 0:
    ost.append((p_a, p_b, p_c))


#print(r)
#print(ost)

i = 0
p_a, p_c = 0, ''
for a, b, c in ost:
    if a == p_a and i < len(r):
        r[i].append(p_c)
        r[i].append(c)
        p_a = 0
        i+=1
        continue
    p_a, p_b, p_c = a, b, c

#print(r)
r_final = r[:i]

for j in range(i, len(r), 2):

    if j < len(r)-1:
        r[j].extend(r[j + 1])
        r_final.append(r[j])

print(len(r_final))
for g in r_final:
    print(" ".join([g[2], g[0]]))
    print(" ".join([g[3], g[1]]))



