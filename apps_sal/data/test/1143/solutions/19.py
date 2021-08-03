w = open('output.txt', 'w')
r = open('input.txt', 'r')
s = [0] * 466
y = [0, 100, 131, 159, 190, 220, 251, 281, 312, 343, 373, 404, 434]
n = int(r.readline())
for i in range(n):
    m, d, p, t = map(int, r.readline().split())
    x = y[m] + d
    s[x] -= p
    s[x - t] += p
for i in range(465):
    s[i + 1] += s[i]
w.write(str(max(s)))
