
[n, m] = list(map(int, input().strip().split()))
wc = [[] for _ in range(4)]
for _ in range(n):
    w, c = list(map(int, input().strip().split()))
    wc[w].append(c)

for i in range(1, 4):
    wc[i].sort(reverse=True)

iwc = [[0 for _ in range(len(wc[i]) + 1)] for i in range(4)]

for i in range(4):
    for j in range(len(wc[i])):
        iwc[i][j + 1] = iwc[i][j] + wc[i][j]

n1 = len(wc[1])
n2 = len(wc[2])
n3 = len(wc[3])

c12 = [(0, 0, 0) for _ in range(m + 1)]
for w in range(len(c12) - 1):
    c, q1, q2 = c12[w]
    c12[w + 1] = max(c12[w + 1], c12[w])
    if q1 < n1:
        c12[w + 1] = max(c12[w + 1], (iwc[1][q1 + 1] + iwc[2][q2], q1 + 1, q2))
    if q2 < n2 and w + 2 < len(c12):
        c12[w + 2] = max(c12[w + 2], (iwc[1][q1] + iwc[2][q2 + 1], q1, q2 + 1))


cmax = 0
for i in range(n3 + 1):
    if 3 * i > m:
        break
    cmax = max(cmax, iwc[3][i] + c12[m - 3 * i][0])

print(cmax)
