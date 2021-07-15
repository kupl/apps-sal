n, m = list(map(int, input().split()))
q = [n]
b = 1
r = 0
i = 0
used = [False] * (2 * 10 ** 4 + 10)
used[n] = True
while i < len(q):
    if i == b:
        b = len(q)
        r += 1
    if q[i] == m:
        print(r)
        break
    if q[i] > 1:
        if not used[q[i] - 1]:
            q.append(q[i] - 1)
            used[q[i] - 1] = True
    if q[i] < m:
        if not used[q[i] * 2]:
            q.append(q[i] * 2)
            used[q[i] * 2] = True
    i += 1

