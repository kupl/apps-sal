aux = [(9000000000.0, 0, 0)]
n = int(input())
for i in range(n):
    (a, b, h) = map(int, input().split())
    aux.append((b, a, h))
aux.sort(reverse=True)
(s, p) = ([0], [0] * (n + 1))
for i in range(1, n + 1):
    while aux[s[-1]][1] >= aux[i][0]:
        s.pop()
    p[i] = p[s[-1]] + aux[i][2]
    s.append(i)
print(max(p))
