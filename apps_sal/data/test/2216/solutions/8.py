n, m, k = map(int, input().split())
d, s, p = 0, [], [list(map(str, range(1, m + 1)))]
p.append(list(reversed(p[0])))
for i in map(str, range(1, n + 1)):
    s += [i + ' ' + j for j in p[d]]
    d = 1 - d
d = 2 * k - 2
for i in range(0, d, 2):
    print(2, s[i] + ' ' + s[i + 1])
print(n * m - d, ' '.join(s[d:]))
